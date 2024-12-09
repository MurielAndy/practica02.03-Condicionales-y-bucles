# Pedimos al usuario su nombre y sexo
 
nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M para mujer, H para hombre): ")
if sexo == "M":
    if nombre[0] < "M":
        print("Perteneces a Gryffindor.")
    else:
        print("Perteneces a Slytherin.")
elif sexo == "H":
    if nombre[0] > "N":
        print("Perteneces a Gryffindor.")
    else:
        print("Perteneces a Slytherin.")
else:
    print("Sexo no válido. Introduce M o H.")

