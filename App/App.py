from flask import Flask, render_template,url_for, request, redirect,jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
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

@app.route('/MTE')
def Mtt():
    return render_template('Modificar_Ticket.html')

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
    
    @app.route('/Mod_Ticket',methods=['POST'])
    def Modificar_Ticket():
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
    
@app.route("/consultar_ticket", methods=["POST"])
def consultar_ticket():
    if request.method == "POST":
        curp = request.json["curp"]

        # Connect to the database
        cursor = mysql.connection.cursor()

        # Query the database for the ticket data
        query = "SELECT * FROM Cita WHERE CURP=%s;"
        cursor.execute(query, (curp,))

        # Fetch the ticket data
        ticketData = cursor.fetchone()

        # Convert the ticket data to JSON
        if ticketData:
            ticketDataJSON = {
                "nombre": ticketData[2],
                "apePater": ticketData[3],
                "apeMater": ticketData[4],
                # ... Add other ticket data fields
            }
            return jsonify(ticketDataJSON)
        else:
            return jsonify({})


def P_N_E(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.register_error_handler(404,P_N_E)
    app.run(debug=True)
    