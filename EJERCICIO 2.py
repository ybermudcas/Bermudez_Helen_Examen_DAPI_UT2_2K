alumnos = {}
opciones = input("Qué opción quieres: (1) añadir alumno, (2) Número de aprobados o (3) Mostrar todo el alumnado?")
#opcion = input("Qué opción quieres: (1) añadir alumno, (2) Número de aprobados o (3) Mostrar todo el alumnado?")

while opciones != "3":
    if opciones =="1":
        nombre = input("Cuál es tú nombre?")
        aprobado_suspendido = input("Introduce <True> si estas aprobado e introduce <False> si estás suspendido")
        parar = input("Escribe <0> si quieres parar de añadir alumno")
        alumnos[nombre]:aprobado_suspendido
        if parar == 0:
            break
        print("El alumno es", nombre, "y está", aprobado_suspendido)

    if opciones == "2":
        count= 0
        for i in range(len(aprobado_suspendido)):
            if i==True:
                count=+1   
            print("El número de aprobados es", count)

    if opciones == "3":
        print(alumnos)