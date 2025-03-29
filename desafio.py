# 1) Solicita ao usuário que digite seu nome

nome = input("Digite o seu nome: ")
if nome.isdigit():
    print("Você digitou seu nome incorretamente!")
    exit()
elif len(nome.strip()) == 0:
    print("Você não digitou nada!")
    exit()

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

try:
    salario = abs(float(input("Digite o seu salário: ").replace(",",".")))
except ValueError:
    print("Você digitou alguma coisa incorreta!")
    exit()
if salario == 0:
    print("Seu salário não pode ser zero!")
    exit()
else:
    pass

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

try:
    percentual = abs(float(input("Digite o seu percentual do bônus: ").replace(",",".")))
except ValueError:
    print("Você digitou alguma coisa incorreta!")
    exit()
if percentual == 0:
    print("Seu percentual de bôuns não pode ser zero!")
    exit()
else:
    pass

# 4) Calcule o valor do bônus final
bonus = 1000 + salario*percentual

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é de {bonus:.2f}")









