from flask import Flask, render_template,url_for, request, redirect,jsonify,session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MPNG'
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'Ticket_Turno'
mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('Index.html')

@app.route('/CTT')
def Ctt():
    return render_template('Crear_Ticket.html')

@app.route('/LogAdm')
def LoginAdm():
    return render_template('Login.html')

@app.route('/Adm', methods=['POST'])
def PagAdm():
    Usuario = request.form['username']
    contraseña = request.form['password']

    cur = mysql.connection.cursor()
    query1 = 'SELECT EXISTS (SELECT * FROM administrador WHERE usuario = %s AND contraseña = %s) AS Acc;'
    cur.execute(query1.encode('UTF-8'), (Usuario.encode('UTF-8'), contraseña.encode('UTF-8')))
    Bol = cur.fetchone()[0]

    if Bol == 1:
        
        return render_template('Pag_Adm.html')
    else:
        return render_template('Login.html')

@app.route('/MTE')
def Mtt():
    DT = None  # Initialize a variable to store DT data

  # Check if DT data is available in the session
    if 'DT' in session:
        DT = session['DT']  # Get DT data from the session

    return render_template('Pag_Adm.html', DT=DT)


@app.route('/Crear_Ticket',methods=['POST'])
def Add_Ticket():
    if request.method == 'POST':
        CURP = request.form['CURP']
        QRT =request.form['QRT']
        Nom_Alm = request.form['nombre']
        Ape_Alm = request.form['Apater']
        Ama_Alm = request.form['Amater']
        Telefono = request.form['telefono']
        Correo = request.form['correo']
        Niv_Cur = request.form['Niv_Cur']
        Asunto = request.form['Asunto']
        Id_Municipio = request.form['Municipio']
        Estado = 'Pendiente'

        try:
            # Connect to the database
            cursor = mysql.connection.cursor()

             # Update the number of appointments for the selected municipality
            query1 = "UPDATE Municipio SET numero_citas = numero_citas + 1 WHERE Id_Municipio=%s;"
            cursor.execute(query1, (Id_Municipio))
            mysql.connection.commit()

            # Get the current number of appointments for the selected municipality
            query2 = "SELECT numero_citas FROM Municipio WHERE Id_Municipio=%s;"
            cursor.execute(query2, (Id_Municipio))
            result = cursor.fetchone()

            # If there is a result, get the number of appointments
            if result:
                num_cita = result[0]

            # Insert the new ticket into the database
            query3 = "INSERT INTO Cita (CURP, Qrt, Nom_Alm, Ape_Alm, Ama_Alm, telefono, correo, Niv_Cur, Asunto, Estado, Num_cita, Id_Municipio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(query3, (CURP, QRT, Nom_Alm, Ape_Alm, Ama_Alm, Telefono, Correo, Niv_Cur, Asunto, Estado, num_cita, Id_Municipio))
            mysql.connection.commit()

            # Check if the ticket was inserted successfully
            if cursor.rowcount > 0:
                # Show success message and assigned ticket number
                print("Se guardó correctamente el nuevo ticket")
                print("Su numero de ticket es: " + str(num_cita))
            else:
                print("Error al registrar")

        except Exception as e:
            print("Error al conectar con la base de datos"+e)

        return redirect(url_for('Index'))
    
@app.route('/Mod_Ticket', methods=["POST"])
def Mod_ticket():
    # Retrieve form data
    CURP = request.form['CURP']
    Qrt = request.form['QRT']
    Nom_Alm = request.form['nombre']
    Ape_Alm = request.form['Apater']
    Ama_Alm = request.form['Amater']
    telefono = request.form['telefono']
    correo = request.form['correo']
    Niv_Cur = request.form['Niv_Cur']
    Asunto = request.form['Asunto']

    try:
        # Connect to the database
        cur2 = mysql.connection
        db = cur2.cursor()

        # Update the ticket data in the database
        query = "UPDATE Cita SET Qrt = %s, Nom_Alm = %s, Ape_Alm = %s, Ama_Alm = %s, telefono = %s, correo = %s, Niv_Cur = %s, Asunto = %s, estado = 'Pendiente' WHERE CURP = %s"
        db.execute(query, (Qrt, Nom_Alm, Ape_Alm, Ama_Alm, telefono, correo, Niv_Cur, Asunto, CURP))
        cur2.commit()

        # Check if the update was successful
        rows_updated = db.rowcount
        if rows_updated > 0:
            # Update successful, display success message
            print('Ticket updated successfully')
        else:
            # Update failed, display error message
            print('Failed to update ticket')

    except Exception as e:
        # Handle database-related errors
        print('Error: ' + e)

    session['DT'] = None
    return redirect(url_for('Index'))

    
@app.route("/consultar_ticket", methods=["POST"])
def consultar_ticket():
    CURP = request.form['CURP']
    Num_Tick = request.form['Num_cita']

    cur = mysql.connection.cursor()
    query1 = 'SELECT EXISTS (SELECT * FROM Cita WHERE CURP = %s AND Num_cita = %s) AS Acc;'
    cur.execute(query1.encode('UTF-8'), (CURP.encode('UTF-8'), Num_Tick.encode('UTF-8')))
    Bol = cur.fetchone()[0]

    if Bol == 1:
        query2 = "SELECT * FROM cita WHERE CURP=%s;"
        cur.execute(query2, (CURP.encode('UTF-8'),))  # Use a tuple to pass the encoded CURP value
        result = cur.fetchone()
         # Store DT data in the session
        session['DT'] = result
        return redirect(url_for('Mtt'))
    else:
       session['DT'] = None
    return redirect(url_for('Mtt'))



def P_N_E(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.register_error_handler(404,P_N_E)
    app.run(debug=True)
    