print("¡Bienvenido al sistema de notas!, por favor, ingrese sus notas consecutivamente, cuando es requerido")
calificacion1 = float(input("¡Ingrese su primera nota!"))
calificacion2 = float(input("¡Ingrese su segunda nota!"))
calificacion3 = float(input("¡Ingrese su tercera nota!"))
calificacion4 = float(input("¡Ingrese su cuarta nota!"))
calificacion5 = float(input("¡Ingrese su quinta nota!"))
 
promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5) / 5

print(f"Tu promedio es {promedio}")

if promedio >= 60: 
    print("Aprobado")
elif promedio >= 40:
    print("En recuperacion")
else:
    print("Reprobado")