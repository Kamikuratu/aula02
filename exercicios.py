import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

#numero_01 = int(input("Insira um número inteiro: "))
#numero_02 = int(input("Insira outro número inteiro: "))
#resultado1 = numero_01 + numero_02
#print(resultado1)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

#numero_03 = int(input("Insira um número inteiro: "))
#resultado2 = numero_03 % 5
#print(resultado2)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

#numero_04 = int(input("Insira um número inteiro: "))
#numero_05 = int(input("Insira outro número inteiro: "))
#resultado3 = numero_04 * numero_05
#print(resultado3)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

#numero_06 = int(input("Insira um número inteiro: "))
#numero_07 = int(input("Insira outro número inteiro: "))
#resultado4 = numero_06 // numero_07
#print(resultado4)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

#numero_08 = int(input("Insira um número inteiro: "))
#resultado5 = numero_08 ** 2
#print(resultado5)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

#numero_09 = float(input("Insira um número flutuante: "))
#numero_10 = float(input("Insira outro número flutuante: "))
#resultado6 = numero_09 + numero_10
#print(resultado6)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

#numero_11 = float(input("Insira um número flutuante: "))
#numero_12 = float(input("Insira outro número flutuante: "))
#resultado7 = (numero_11 + numero_12)/2
#print(resultado7)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

#numero_13 = float(input("Insira a base: "))
#numero_14 = float(input("Insira o expoente: "))
#resultado8 = numero_13 ** numero_14
#print(resultado8)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

#temp_celsius = float(input("Insira a temperatura em graus Celsius: "))
#temp_fahrenheit = (temp_celsius * (9/5))+32
#print(temp_fahrenheit)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

#raio = float(input("Insira o raio do círuclo: "))
#area = (raio ** 2)*math.pi
#print(area)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

#string_1 = str(input("Insira uma string: "))
#string_1_maiuscula = string_1.upper()
#print("A string toda maiúscula é: ", string_1_maiuscula)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

#string_2 = str(input("Insira seu nome completo: "))
#string_2_minuscula = string_2.lower()
#print("Seu nome completo minúsculo é: ", string_2_minuscula)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

#string_3 = input("Insira uma frase: ")
#string_3_sem_espacos = string_3.strip()
#print("A frase sem espaços em branco no início e no final é: ", string_3_sem_espacos)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

#data = input("Digite uma data no formato dd/mm/aaaa: ")
#dia, mes, ano = data.split("/")
#print("Dia: ", dia)
#print("Mês: ", mes)
#print("Ano: ", ano)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

#string_4 = input("Digite uma palavra: ")
#string_5 = input("Digite outra palavra: ")
#concat = string_4 + string_5
#print("As palavras concatenadas são: ", concat)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

#bool1 = bool(input("Digite um booleano: "))
#bool2 = bool(input("Digite outro booleano: "))
#op_and = bool1 and bool2
#print("O resultado da operação and é: ", op_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

#bool3 = bool(input("Digite um booleano: "))
#bool4 = bool(input("Digite outro booleano: "))
#op_or = bool3 or bool4
#print("O resultado da operação or é: ", op_or)


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

#bool5 = bool(input("Insira um booleano: "))
#op_not = not bool5
#print("O valor booleano invertido é: ", op_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

#num1 = int(input("Insira um número: "))
#num2 = int(input("Insira um número: "))
#op_equal = num1 == num2
#print("Os números são iguais? ", op_equal)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

#num1 = int(input("Insira um número: "))
#num2 = int(input("Insira um número: "))
#op_equal = num1 != num2
#print("Os números são diferentes? ", op_equal)

# #### try-except e if

# 21: Conversor de Temperatura

#try:
#    temp_celsius = float(input("Insira a temperatura em graus Celsius: "))
#    temp_fahrenheit = (temp_celsius * (9/5))+32
#    print(temp_fahrenheit)
#except ValueError:
#    print("O valor informado não é um número!")

# 22: Verificador de Palíndromo

#string = input("Insira uma palavra que deseja checar se é um palíndromo: ")
#if isinstance(string, str):
#    formatado = string.replace(" ", "").lower()
#    if string == string[::-1]:
#        print("A palavra é um palíndromo!")
#    else:
#        print("A palavra não é um palíndromo!")
#else:
#    print("Você não informou uma palavra!")

# 23: Calculadora Simples
#try:
#    numero1 = float(input("Insira um número: "))
#    numero2 = float(input("Insira outro número: "))
#    operador = input("Qual operação você deseja realizar?: ")
#
#    if operador == "+":
#        adicao = numero1 + numero2
#        print("O resultado da soma é: ", adicao)
#    elif operador == "-":
#        subtracao = numero1 - numero2
#        print("O resultado da subtração é: ", subtracao)
#    elif operador == "*":
#        multiplicacao = numero1 * numero2
#        print("O resultado da multiplicação é: ", multiplicacao)
#    elif operador == "/":
#        try:
#            divisao = numero1 * numero2
#            print("O resultado da divisão é: ", divisao)
#        except ZeroDivisionError:
#            print("Não é possível dividir por zero!")
#    else:
#        print("Você não informou uma operação válida!")
#except ValueError:
#    print("Você não informou um número válido!")


# 24: Classificador de Números

#try:
#    numero = int(input("Digite um número: "))
#    if numero == 0:
#        print("O número é zero!")
#    elif numero > 0:
#        if numero%2 == 0:
#            print("O número é positivo e par!")
#        else:
#            print("O número é positivo e ímpar!")
#    else:
#        if numero%2 == 0:
#            print("O número é negativo e par!")
#        else:
#            print("O número é negativo e ímpar!")
#except ValueError:
#    print("Você não informou um número válido!")


# 25: Conversão de Tipo com Validação

lista = input("Insira uma lista de números inteiros separados por vírgula: ")
lista_str = lista.split(",")
lista_int = []

try:
    for num in lista_str:
        lista_int.append(int(num.strip()))
    print("A lista de números inteiro é: ", lista_int)
except ValueError:
    print("Você inseriu algum número inválido!")