"""
#EX1

entrada = input("numero: ")
num = int(entrada)
if num > 10:
    print("é 10")
    else:
        print(f"{num} é de fato um numero")

#EX2

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

EX4
time1 = input("Primeiro time: ")
gols1 = input("Seus gols: ")
num1 = int(gols1)
time2 = input("Segundo time: ")
gols2 = input("Seus gols: ")
num2 = int(gols2)
if num1 > num2:
    print(f"O {time1} é o vencedor, tendo {gols1}")
elif num2 > num1: 
    print(f"O {time2} é o vencedor, tendo {gols2}")
else: 
    print(f"Empate")

#EX5

"""

















"""entrada = input("Digite Nmr Int")
num = int(entrada)
resto = num % 2
if resto == 0:
    print(f"{num} par")

else:
    print(f"{num} impar")
"""

"""entrada = input("numero: ")
num = int(entrada)
if num > 10:
    print("positivo")
elif num < 0:
    print("negativo")
else:
    print(str(num) + "é 0")


3.3
numero1 = float(input("Primeiro numero: "))
op = input("Digite o operador (+-*/): ")
numero2 = float(input("Segundo numero: "))

if op == '+':
    resultado = numero1 + numero2
elif op == '-':
    resultado = numero1 - numero2
elif op == '*':
    resultado = numero1 * numero2
elif op == '/': 
    resultado = numero1 / numero2
else:
    print("Operador invalido")
print(f"O resultado é {resultado}")
"""