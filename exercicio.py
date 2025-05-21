import math 
# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
""" 
try:
    numero_01 = int(input("Inserir um numero inteiro: "))
    numero_02 = int(input("Inserir um numero inteiro: "))
    result = numero_01+numero_02

    print(f"Resultado da soma do numero {numero_01} pelo {numero_02} é igual a {result}") 
except TypeError as e:
    print(e)
 """
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
""" 
try:
    numero_01 = int(input("Inserir um numero inteiro: "))
    result = numero_01%5
    print(f"Resultado do resto da divisao do numero {numero_01} pelo numero 5 é igual a {result}") 
except TypeError as e:
    print(e)
     """
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
""" 
try:
    numero_01 = int(input("Inserir um numero inteiro: "))
    numero_02 = int(input("Inserir um numero inteiro: "))
    result = numero_01*numero_02

    print(f"Resultado da multiplicação do numero {numero_01} pelo {numero_02} é igual a {result}") 
except TypeError as e:
    print(e)
 """
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
""" 
try:
    numero_01 = int(input("Inserir um numero inteiro: "))
    numero_02 = int(input("Inserir um numero inteiro: "))
    result = numero_01//numero_02

    print(f"Resultado da divisão inteira do numero {numero_01} pelo {numero_02} é igual a {result}") 
except TypeError as e:
    print(e)
 """
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# try:
#     numero_01 = int(input("Inserir um numero inteiro: "))
#     numero_02 = int(input("Inserir um numero inteiro: "))
#     result = numero_01//numero_02

#     print(f"Resultado da divisão inteira do numero {numero_01} pelo {numero_02} é igual a {result}") 
# except TypeError as e:
#     print(e)
    
# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
try:
    numero_01 = float(input("Inserir um numero real: "))
    numero_02 = float(input("Inserir um numero real: "))
    result = numero_01 + numero_02

    print(f"Resultado da soma real do numero {numero_01} pelo {numero_02} é igual a {result}") 
except TypeError as e:
    print(e)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

try:
    numero_01 = float(input("Inserir um numero real: "))
    numero_02 = float(input("Inserir um numero real: "))
    result = (numero_01 + numero_02)/2

    print(f"Resultado da media é igual a {result}") 
except TypeError as e:
    print(e)
    
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

"""
 raio_circulo = float(input("Digite o raio: "))
area = math.pi * raio_circulo ** 2 

print(f"{area:.2f}")
 """
# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#data = "20/02/2024"
""" 
try:
    data = input("Insira uma data no formato dd/mm/yyyy: ")

    data_separada = data.split("/")
    print(data_separada)
except:
    print("Formanto incorreto")
 """
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
