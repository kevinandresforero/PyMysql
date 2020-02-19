import pymysql.cursors

Db = "Prueba"
contraseña = "enlacasa"
op = 0

while op != 8:
    print("\n")
    print("1. Crear base de datos")
    print("2. Crear tabla")
    print("3. Agregar estudiante")
    print("4. Listar tabla")
    print("5. Listar un estudiante")
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
                            Codigo BIGINT(13) NOT NULL,
                            Nota1 FLOAT(4) DEFAULT NULL,
                            Nota2 FLOAT(4) DEFAULT NULL,
                            Nota3 FLOAT(4) DEFAULT NULL,
                            NotaFinal FLOAT(4) DEFAULT NULL,
                            PRIMARY KEY(Codigo)
            ) ;"""
            cursor.execute(CrearTabla)
            conexion.commit()
            print("Creada Tabla Estudiantes Satisfactoriamente")
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

        Codigo = int(input("Digite codigo del estudiante: "))

        MostarTabla1 = "select * from Estudiantes\
            where Codigo=%s"
        cursor.execute(MostarTabla1, (Codigo, ))
        cursor.fetchone()
        if cursor.rowcount >= 1:
            print("Ya existe el estudiante "+str(Codigo))
            cursor.close()
            conexion.close()
        else:
            Nombre = input("Digite nombre del estudiante: ")
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
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            passwd=contraseña,
            database=Db
        )

        try:
            MostrarTabla = "select * from Estudiantes"
            cursor = conexion.cursor()
            cursor.execute(MostrarTabla)
            record = cursor.fetchall()
            print("---> Numero de filas: ", cursor.rowcount)
            for fila in record:
                print("{:<4} {:<4} {:<4} {:<4} {:<4} {:<4} ".format(fila[0], fila[1], 
                fila[2], fila[3], fila[4], fila[5]))
            cursor.close()
            conexion.close()

        except:
            print("Error en conexion")
    
    elif op == 5:
        print("Listar un estudiante")
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            passwd=contraseña,
            database=Db
        )

        try: 
            MostarTabla1 = "select * from Estudiantes\
                where  Codigo=%s"
            cursor = conexion.cursor()
            Codigo = int(input("Digite codigo del estudiante: "))

            cursor.execute(MostarTabla1, (Codigo, ))
            fila = cursor.fetchone()
            print("---> Numero de filas: ", cursor.rowcount)
            if cursor.rowcount == 0:
                print ("No existe estudiante"+str(Codigo))
            else:
                print("Nombre = ", fila[0])
                print("Codigo = ", fila[1])
                print("Nota1= ", fila[2])
                print("Nota2 = ", fila[3])
                print("Nota3 = ", fila[4])
                print("NotaFinal = ", fila[5])
            cursor.close()
            conexion.close()

        except:
           print("Error en conexion")  

    elif op == 6:
        print("Actualizar nota de un estudiante")
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            passwd=contraseña,
            database=Db
        )

        #try: 
        MostarTabla1 = "select * from Estudiantes\
            where  Codigo=%s"
        cursor = conexion.cursor()
        Codigo = int(input("Digite codigo del estudiante: "))
        cursor.execute(MostarTabla1, (Codigo, ))
        fila = cursor.fetchone()
        print("---> Numero de filas: ", cursor.rowcount)
        if cursor.rowcount == 0:
            print ("No existe estudiante"+str(Codigo))
        else:
            Nota1 = int(input("Digite Nota1 del estudiante: "))
            Nota2 = int(input("Digite Nota2 del estudiante: "))
            Nota3 = int(input("Digite Nota3 del estudiante: "))

            #actualiza = "update Estudiantes set Nota1 =%s where Codigo = %s"
            """actualiza = "update Estudiantes set Nota2 =%s where Codigo = %s"
            actualiza = "update Estudiantes set Nota3 =%s where Codigo = %s"
            cursor.execute(actualiza, (Nota1, Codigo))
            cursor.execute(actualiza, (Nota2, Codigo))
            cursor.execute(actualiza, (Nota2, Codigo))"""

            sql = "UPDATE Estudiantes SET Nota1 = %s WHERE Nota1 = %s"
            val = ("Nota1,")

            cursor.execute("SELECT COUNT(*) FROM Estudiantes WHERE Codigo IN(Nota1, Nota2, Nota3)")
            cursor.execute("UPDATE Estudiantes SET Value=0 WHERE Codigo IN(Nota1, Nota2, Nota3)")
            
            conexion.commit()
            NotaFinal = float(Nota1) * 0.35 + float(Nota2) * 0.35 + float(Nota3) * 0.30
            #InsertarRegistro = """insert into Estudiantes(Nombre, Codigo, Nota1, Nota2, Nota3, NotaFinal) values
            #(%s,%s,%s,%s,%s,%s)"""

            
            print("Notas actualizadas")
            cursor.close()
            conexion.close()
        #except:
         #   print("Error durante el proceso")

"""
otro
cursor1.execute("select codigo, descripcion, precio from articulos")
for fila in cursor1:
    print(fila)

otro
cursor1.execute("delete from articulos where codigo=1")
cursor1.execute("update articulos set precio=50 where codigo=3")

"""
