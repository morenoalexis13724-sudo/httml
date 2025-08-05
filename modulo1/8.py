print("SIstema de calificación de notas ejercicio3")
nota = float(input("Introduce la nota del estudiante: "))
if nota >= 90:
    print("A")
elif 80 <= nota < 90:
    print("B")
elif 70 <= nota < 80:
    print("C")
elif 60 <= nota < 70:
    print("D")
else:
    print("F")