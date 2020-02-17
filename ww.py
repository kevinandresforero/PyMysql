import pymysql.cursors

conexion = pymysql.connect(host="localhost",
                           user="root",
                           passwd="261120",
                           database="Prueba")

cursor = conexion.cursor()

tabla = """CREATE TABLE Estudiantes(
    Nombre Char(30) NOT NULL,
    Codigo INT(11) NOT NULL,
    Nota1 FLOAT(4) DEFAULT NULL,
    Nota2 FLOAT(4) DEFAULT NULL,
    Nota3 FLOAT(4) DEFAULT NULL,
    PRIMARY KEY(Codigo)
) ;
"""
try:
    cursor
    print("\nSe Pudo Conectar con la DB")
except:
    print("\nNo Se Pudo Conectar con la DB")
try:
    cursor.execute(tabla)
    print("\nSe acaba de crear la DB")
except:
    print("\n Ya estaba creada la DB")
