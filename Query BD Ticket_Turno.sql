-- Crear la base de datos
CREATE DATABASE Ticket_Turno;

-- Crear la tabla Administrador
use Ticket_Turno;
CREATE TABLE Administrador (
    id_administrador INT AUTO_INCREMENT PRIMARY KEY,
    usuario INT(10) NOT NULL,
    contraseña VARCHAR(50) NOT NULL
);

-- Crear la tabla Municipio
use Ticket_Turno;
CREATE TABLE Municipio (
    Id_Municipio INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(25) NOT NULL,
    numero_citas INT NOT NULL
);

-- Crear la tabla Cita
use Ticket_Turno;
CREATE TABLE Cita (
    CURP VARCHAR(18) NOT NULL PRIMARY KEY,
    Qrt VARCHAR(12) NOT NULL,
    Nom_Alm VARCHAR(15) NOT NULL,
    Ape_Alm VARCHAR(15) NOT NULL,
    Ama_Alm VARCHAR(15) NOT NULL,
    Telefono VARCHAR(10) NOT NULL,
    Correo VARCHAR(50) NOT NULL,
    Niv_Cur VARCHAR(15) NOT NULL,
    Asunto TEXT NOT NULL,
    Estado VARCHAR(10) NOT NULL,
    Num_cita INT NOT NULL,
    Id_Municipio INT NOT NULL,
    FOREIGN KEY (Id_Municipio) REFERENCES Municipio(Id_Municipio)
);

use Ticket_Turno;
 ALTER TABLE Cita
    ADD CONSTRAINT fk_Cita_Municipio
	FOREIGN KEY (Id_Municipio)
	REFERENCES Municipio (Id_Municipio);
    
    -- Insertar datos en la tabla Municipio
INSERT INTO Municipio (Nombre, numero_citas) VALUES
    ('Abasolo', 0),
    ('Acuña', 0),
    ('Allende', 0),
    ('Arteaga', 0),
    ('Candela', 0),
    ('Castaños', 0),
    ('Cuatro Ciénegas', 0),
    ('Escobedo', 0),
    ('Francisco I. Madero', 0),
    ('Frontera', 0),
     ('General Cepeda', 0),
    ('Guerrero', 0),
    ('Hidalgo', 0),
    ('Jiménez', 0),
    ('Juárez', 0),
    ('Lamadrid', 0),
    ('Matamoros', 0),
    ('Monclova', 0),
    ('Morelos', 0),
    ('Múzquiz', 0),  
     ('Nadadores', 0),
    ('Nava', 0),
    ('Ocampo', 0),
    ('Parras', 0),
    ('Piedras Negras', 0),
    ('Progreso', 0),
    ('Ramos Arizpe', 0),
    ('Sabinas', 0),
    ('Sacramento', 0),
    ('Saltillo', 0),  
     ('San Buenaventura', 0),
    ('San Juan de Sabinas', 0),
    ('San Pedro', 0),
    ('Sierra Mojada', 0),
    ('Torreón', 0),
    ('Viesca', 0),
    ('Villa Unión', 0),
    ('Zaragoza', 0);
    




