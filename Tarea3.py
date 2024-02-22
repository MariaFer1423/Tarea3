def suma(num_1, num_2):
    return num_1 + num_2


if __name__ == "__main__":
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        resultado = suma(num1, num2)
        print("La suma es:", resultado)
    except ValueError:
        print("Error: Ingrese números válidos.")
