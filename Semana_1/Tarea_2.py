#Tarea 01 parte 1
#Escribir la frase Hello world
print("Hello, World!") 

#Tarea 01 parte 2
# Solicitar al usuario dos números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Mostrar menú de operaciones
print("\nElige una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Introduce el número de la operación (1-4): ")

# Realizar operación según la opción elegida
if opcion == "1":
    resultado = num1 + num2
    print(f"La suma de {num1} y {num2} es: {resultado}")
elif opcion == "2":
    resultado = num1 - num2
    print(f"La resta de {num1} y {num2} es: {resultado}")
elif opcion == "3":
    resultado = num1 * num2
    print(f"La multiplicación de {num1} y {num2} es: {resultado}")
elif opcion == "4":
    if num2 != 0:
        resultado = num1 / num2
        print(f"La división de {num1} entre {num2} es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")