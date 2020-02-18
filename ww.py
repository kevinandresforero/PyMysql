import pymysql.cursors

Db = "Prueba"
contraseña = "261120"
op = 0

while op != 8:
    print("\n")
    print("1. Crear base de datos")
    print("2. Crear tabla")
    print("3. Instertar un registro")
    print("4. Listar tabla")
    print("5. Listar una sola fila")
    print("6. Actualiza un registro")
    print("7. Retira un registro")
    print("8. Termina\n")
    op = int(input("Digite opcion: "))

    if op == 1:
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            passwd=contraseña,
        )
        cursor = conexion.cursor()
        cursor.execute("SHOW DATABASES;")
        print("Conectado Ome")
        try:
            print("Creando...")
            cursor.execute("CREATE DATABASE Prueba;")
            print("\n")
        except:
            print("Se creo satisfactoriamente la DB Prueba")
        cursor.close()


    elif  op == 2:
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            passwd=contraseña,
            database=Db
        )
        cursor = conexion.cursor()
        #cursor.execute("SHOW DATABASES;")
        print("Conectado Ome")
        try:
            CrearTabla = """CREATE TABLE Estudiantes(
                            Nombre Char(30) NOT NULL,
                            Codigo INT(11) NOT NULL,
                            Nota1 FLOAT(4) DEFAULT NULL,
                            Nota2 FLOAT(4) DEFAULT NULL,
                            Nota3 FLOAT(4) DEFAULT NULL,
                            NotaFinal FLOAT(4) DEFAULT NULL,
                            PRIMARY KEY(Codigo)
            ) ;"""
            cursor.execute(CrearTabla)
            conexion.commit()
            print("Cread Tabla Estudiantes")
        except:
            print("la Tabla Estudiantes Ya Existe")
        cursor.close()
        conexion.close()

    elif  op == 3:
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            passwd=contraseña,
            database=Db
        )

        cursor = conexion.cursor()

        Nombre = input("Digite nombre del estudiante: ")
        Codigo = input("Digite codigo del estudiante: ")
        Nota1 = input("Digite nota del Corte 1: ")
        Nota2 = input("Digite nota del Corte 2: ")
        Nota3 = input("Digite nota del Corte 3: ")
        NotaFinal = float(Nota1) * 0.35 + float(Nota2) * 0.35 + float(Nota3) * 0.30

        InsertarRegistro = """insert into Estudiantes(Nombre, Codigo, Nota1, Nota2, Nota3, NotaFinal) values
         (%s,%s,%s,%s,%s,%s)"""
        cursor.execute(InsertarRegistro, (Nombre, Codigo, Nota1, Nota2, Nota3, NotaFinal))
        print("Registro Agregado <3")
        cursor.close()
        conexion.commit()

    elif op==4:
        print("Cuarta opción")


"""try:
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

InsertarRegistro = "insert into Estudiantes(Nombre, Codigo, Nota1, Nota2, Nota3, NotaFinal) values (%s,%s,%s,%s,%s,%s)"
cursor.execute(InsertarRegistro, (Nombre, Codigo, Nota1, Nota2, Nota3, NotaFinal))
cursor.close()
conexion.commit()"""
