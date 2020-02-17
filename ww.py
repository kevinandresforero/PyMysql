import pymysql.cursors

conexion = pymysql.connect(host="localhost",
                           user="root",
                           passwd="",           #   contraseña de la base de datos
                           database="alumno")   # nombre de la base de datos local ya creada

cursor = conexion.cursor()

tabla = """CREATE TABLE Estudiantes(
    Nombre Char(30) NOT NULL,
    Codigo INT(11) NOT NULL,
    Nota1 FLOAT(4) DEFAULT NULL,
    Nota2 FLOAT(4) DEFAULT NULL,
    Nota3 FLOAT(4) DEFAULT NULL,
    NotaFinal FLOAT(4) DEFAULT NULL,
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

Nombre = input("Digite nombre del estudiante: ")
Codigo = input("Digite codigo del estudiante: ")
Nota1 = input("Digite nota del Corte 1: ")
Nota2 = input("Digite nota del Corte 2: ")
Nota3 = input("Digite nota del Corte 3: ")
NotaFinal = float(Nota1)*0.35 + float(Nota2)*0.35 + float(Nota3)*0.30 

print(Nombre)
print(NotaFinal)

