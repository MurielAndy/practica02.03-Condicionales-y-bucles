#Cantidad de  veces de la letra que hay en la frase

n = []
frase_introducida= input("Introduce una frase:")
letra_introducida = input("Introduce una letra:")
n.append(frase_introducida)
cantidad_de_veces=frase_introducida.count(letra_introducida)
print("La cantidad de la letra que hay en la frase es:",cantidad_de_veces)