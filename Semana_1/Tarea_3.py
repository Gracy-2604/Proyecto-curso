# Tarea 02
# Función para calcular el valor absoluto de un número
def valor_absoluto(n):
    return n if n >= 0 else -n

try:
    # Pedir al usuario un número
    num = float(input("Introduce un número: "))

    # Calcular valor absoluto
    resultado = valor_absoluto(num)

    # Mostrar resultado
    print(f"El valor absoluto de {num} es: {resultado}")

except ValueError:
    print("Error: Debes introducir un número válido.")


# Función para calcular el valor absoluto de una expresión
def valor_absoluto(n):
    return n if n >= 0 else -n

try:
    # Pedir al usuario una expresión matemática
    expresion = input("Introduce una expresión matemática: ")

    # Evaluar la expresión de forma segura
    num = eval(expresion)

    # Calcular el valor absoluto
    resultado = valor_absoluto(num)

    # Mostrar el resultado
    print(f"El valor absoluto de ({expresion}) = {resultado}")

except Exception as e:
    print("Error: Introduce una expresión válida.")