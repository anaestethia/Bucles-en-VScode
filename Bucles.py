numeros_ingresados = []

while True:
    numero = float(input("Ingrese un número (cuando termine ingrese 0): "))
    numeros_ingresados.append(numero)
    if numero == 0:
      break 

suma = sum(numeros_ingresados)
promedio = suma / len(numeros_ingresados)

print(f"La suma de los números ingresados es: {suma}")
print(f"El promedio de los números ingresados es: {promedio}")