import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS laboratorio")

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "laboratorio"
)

cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tipoMedicamento (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, tipo VARCHAR(50) NOT NULL, activo BOOLEAN)")
cursor.execute("CREATE TABLE IF NOT EXISTS medicamento (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, codigoAlfabetico VARCHAR(3) NOT NULL, codigoNumerico INT NOT NULL, codigoVerificador INT NOT NULL, nombre VARCHAR(50) NOT NULL, droga VARCHAR(50) NOT NULL, tipoMedicamento INT NOT NULL, FOREIGN KEY (tipoMedicamento) REFERENCES tipoMedicamento (id))")