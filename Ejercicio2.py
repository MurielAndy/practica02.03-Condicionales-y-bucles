# Pedimos al usuario que ingrese dos números
 
  
numerador = float(input("Introduce el numerador: "))
divisor = float(input("Introduce el divisor: "))
if divisor == 0:
    +print("Error: No se puede dividir entre cero.")
else:
    resultado = numerador / divisor
    print("El resultado de la división es:", resultado)
