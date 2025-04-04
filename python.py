"""
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
"""


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
diasU = int(input("dias uteis: "))
horas_T = int(input("hrs trabalhadas: "))
valorPH = int(input("valor por hr: "))

jornadaM = diasU * 8

if horas_T > jornadaM:
    horas_ex = horas_T - jornadaM
    valorHr_ex = valorPH * 1.5
    valor_ex = horas_ex * valorHr_ex
else:
    horas_extras = 0
    valor_ex = 0

if horas_T > jornadaM:
    salario = jornadaM * valorPH
else:
    salario = horas_T + valor_ex

salarioT = salario + valor_ex

print(f"Horas extras: {horas_ex}")
print(f"valor extra: {valor_ex}")
print(f"salario total: R${salario}")

EX ?????
dia = int(input("Dia: "))
mes = int(input("Mês: "))

if dia < 1 or dia > 31 or mes <1 or mes > 12:
    print("invalido")
elif mes == 2 and dia > 28:
    print("invalido")
elif dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("invalido")
else:
    print("valido")
    
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