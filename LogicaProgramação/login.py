# numero_tentivas = 3
# for tentiva in range(numero_tentivas):
#     usuario = input("Digite usario para acesso")
#     senha = input("Digite senha para acesso")
#     if usuario == "jhonathan" and senha == "123":
#         print("Acesso liberado")
#         break
#     else:
#         print(f"Erro de login, {tentiva + 1} de {numero_tentivas} Erro de login. Tente novamente.")
# else:
#     print("Limite de tentativas excedido. Acesso bloqueado.")
# FEITO DIA 25/03/2024

# Escreva um programa que peça ao usuário para digitar números inteiros positivos. O
# programa deve somar esses números até que o usuário digite '0'. Quando '0' for digitado, o
# programa deve parar de pedir números e imprimir a soma total.

# num = 0
# while True:
#     numer_int = int(input("Digite numeros positivos"))
#     if numer_int < 0:
#         print("erro, digite outro numero acima de zero")
#         continue
#     elif numer_int > 0:
#         num += numer_int
#     elif numer_int == 0:
#         print(f"Soma total de numeros informados é {num}")
#         break
# feito dia 25/04/2025

for i in range(1, 6):
    print(f"TABALA DE MULTIPLICAÇÃO{i}")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")




