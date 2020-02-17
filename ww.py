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

nom = input("Digite nombre del estudiante: ")
cod = input("Digite codigo del estudiante: ")
n1 = input("Digite nota del Corte 1: ")
n2 = input("Digite nota del Corte 2: ")
n3 = input("Digite nota del Corte 3: ")
nf = float(n1)*0.35 + float(n2)*0.35 + float(n3)*0.30 

print(nom)
print(nf)

"""
#cursor=conexion.cursor()
sql="insert into Estudiantes(Nombre, Codigo, Nota1, Nota2, Nota3, NotaFinal) values (%s,%s,%s,%s,%s,%s)"
datos=(nom, cod, n1, n2, n3, nf)
cursor.execute(sql, datos)
#datos=("peras", 34)
#cursor1.execute(sql, datos)
#datos=("bananas", 25)
#cursor1.execute(sql, datos)
#conexion.commit()
conexion.close()"""  