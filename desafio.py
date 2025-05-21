import re

CONSTANTE_BONUS = 1000

######################################### 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite seu Nome: ")

if nome_usuario.isdigit():
    print("Voce digitou o seu nome errado")
    exit()
elif len(nome_usuario)==0:
    print("Voce não digitou nada")
    exit()
elif nome_usuario.isspace():
    print("Voce só digitou espaço")
    exit()    
elif re.fullmatch(r"[^\w\s]+", nome_usuario):
    print("Você digitou apenas caracteres especiais.")
    exit()     

#nome_usuario = "33"
#print(nome_usuario.isdigit())

######################################### 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario_usuario = float(input("Digite o valor do seu salário: "))
    if salario_usuario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()

######################################### 3) Solicita ao usuário que digite o valor do bônus recebido

# Converte a entrada para um número de ponto flutuante
#bonus_usuario = float(input("Digite seu Bonus: "))

try:
    bonus_usuario = float(input("Digite o valor do bônus recebido: "))
    if  bonus_usuario > 20 or bonus_usuario <= 0:

        print("Por favor, digite um valor positivo maior que zero e menor igual a 20 para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()

######################################### 4) Calcule o valor do bônus final
valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

######################################### 5) Imprima cálculo do KPI para o usuário
#print(f"O usuario: {nome_usuario} possui o bonus: {valor_bonus}")
print(f"{nome_usuario}, seu salário é R${salario_usuario:.2f} e seu bônus final é R${valor_bonus:.2f}.")

######################################### 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

######################################### Bônus: Quantos bugs e riscos você consegue identificar nesse programa?