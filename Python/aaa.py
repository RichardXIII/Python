numero1 = input("Primeiro numero: ")
num1 = int(numero1)
numero2 = input("Segundo numero: ")
num2 = int(numero2)
if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num2 >num1:
    print(f"{num2} é maior que {num1}")
else:
    print(f"Ambos os numeros {num1} e {num2} são iguais")
