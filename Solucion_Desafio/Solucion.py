print("¡Bienvenido al sistema de notas!, por favor, ingrese sus notas consecutivamente, cuando es requerido")
calificacion1 = int(input("¡Ingrese su primera nota!"))
calificacion2 = int(input("¡Ingrese su segunda nota!"))
calificacion3 = int(input("¡Ingrese su tercera nota!"))
calificacion4 = int(input("¡Ingrese su cuarta nota!"))
calificacion5 = int(input("¡Ingrese su quinta nota!"))

promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5)

if promedio >= 1: 
    print("ganaste")