import pymysql.cursors

contraseña = "laencasa"
Db = "Prueba1"

conexion = pymysql.connect(host="localhost",
                           user="casa",
                           passwd=contraseña,
                           database=Db)

op = 0
cursor = conexion.cursor()

while op != 9:
    print("\n1. Crear Base de datos")
    print("2. Crear Tabla Students")
    print("3. Crear Tabla Materias")
    print("4. Crear Tabla Relaciones")
    print("5. Llenar tabla Students")
    print("6. Llenar tabla Materias")
    print("7. Llenar Relaciones")
    print("8. Mostrar Tablas")
    print("9. Borrar Tabla\n")
    op = int(input("Digite opcion: "))

    if op == 1:         # Crear base de datos
        cursor = conexion.cursor()
        print("\nConectado") 
        cursor.execute("SHOW DATABASES;")
        try:
            cursor.execute("CREATE DATABASE Prueba;")
            print("\nCreando...")
            print("\nSe creo satisfactoriamente la DB Prueba")
            conexion.commit()
        except:
            print("\nYa Fue Creada En Otra Ocación la DB Prueba")

    if op == 2:         #Crear tabla Estudiantes
        try:
            Students = """CREATE TABLE Students(
                            IdE int NOT NULL,
                            NomE varchar(15) NOT NULL,
                            PRIMARY KEY(IdE)
            ) ;
            """
            cursor.execute(Students)
            print("\nCreando tabla Students...")
            print("\nTabla Students  creada satisfactoriamente")
            conexion.commit()
        except:
            print("\nTabla Students ya existe")

    if op == 3:         #Crear tabla Materias
        cursor = conexion.cursor()
        try:
            Materias = """CREATE TABLE Materias(
                        idM int NOT NULL,
                        NomM varchar(15) NOT NULL,
                        PRIMARY KEY(idM)
            ) ;
            """
            cursor.execute(Materias)
            print("\nCreando tabla Materias...")
            print("\nTabla Materias  creada satisfactoriamente")
            conexion.commit()
        except:
            print("\nTabla Materias ya existe")

    if op == 4: #Crear tabla relaciones
        try:
            Relaciones = """CREATE TABLE Relaciones(
                            idE_foran int NOT NULL,
                            idM_foran int NOT NULL,
                            FOREIGN KEY (idE_foran) REFERENCES Students(IdE),
                            FOREIGN KEY (idM_foran) REFERENCES Materias(idM)
                            );"""
            cursor.execute(Relaciones)
            print("\nCreando tabla Relaciones...")
            print("\nTabla Relaciones creada satisfactoriamente")
            conexion.commit()
        except:
            print("\nYa está creada la tabla Relaciones")

    if op == 5: #Llenar tabla Students
        try:
            IdE = int(input("Digite codigo del estudiante: "))
            NomE = input("Digite nombre del estudiante: ")
            TablaAlumnos = """INSERT INTO Students(IdE, NomE) VALUES(%s, %s)"""
            cursor.execute(TablaAlumnos, (IdE, NomE))
            print("\nRegistro agregado")
            conexion.commit()
        except:
            print("\nError al agregar registro")

    if op == 6: #Llenar tabla Materias
        try:
            IdM = int(input("Digite codigo de la materia: "))
            NomM = input("Digite nombre de la materia: ")
            TablaMaterias = """INSERT INTO Materias(IdM, NomM) VALUES(%s, %s)"""
            cursor.execute(TablaMaterias, (IdM, NomM))
            print("\nRegistro agregado")
            conexion.commit()
        except:
            print("\nError al agregar registro") 
    
    if op == 7: #Llenar tabla Relaciones
        cursor = conexion.cursor()
        try:
            idM_foran = int(input("Digite codigo de la materia: "))
            idE_foran = int(input("Digite codigo del estudiante: "))
            TablaRelaciones = """INSERT INTO Relaciones(idM_foran, idE_foran) VALUES (%s, %s)"""
            cursor.execute(TablaRelaciones, (idM_foran, idE_foran))
            print("\nRegistro agregado")
            conexion.commit()        
        except:
            print("\nError al procesar registro")

    if op == 8:     #Mostrar tablas
        try:
            MostrarTablaEs = "select * from  Students"
            cursor.execute(MostrarTablaEs)
            record = cursor.fetchall()
            for fila in record:
                print("{:<4} {:<4}".format(fila[0], fila[1]))
            print("\n")
            
        except:
            print("\n Error al mostrar tabla Estudiantes")

        try:
            MostrarTablaMa = "select * from  Materias"
            cursor.execute(MostrarTablaMa)
            record = cursor.fetchall()
            for fila in record:
                print("{:<4} {:<4}".format(fila[0], fila[1]))  
            print("\n")

        except:
            print("\n Error al mostrar Materias")

        try:
            MostrarTablaRe = "select IdE, IdM, NomE, NomM from Students\
                inner join Relaciones on Relaciones.idE_foran = Students.IdE\
                inner join Materias on Relaciones.idM_foran = Materias.idM"
            cursor.execute(MostrarTablaRe)
            record = cursor.fetchall()
            for fila in record:
                print("{:<4} {:<4}".format(fila[0], fila[1]))

            
        except:
            print("\n Error al mostrar Relaciones")
        #cursor.close()
        #conexion.close()