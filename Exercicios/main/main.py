from Exercicios.main.metodos import Mathe

# ALTE + ENTER ///  PARA IMPORTA A CLASS FACILMENTE

print("\tBEM VINDO")
print("---------------------------------------")
print("\tPROJETO CALCULADORA")
print()
print("Escolha 1 para SOMAR")
print("Escolha 2 para SUBTRAIR")
print("Escolha 3 para DIVIDIR")
print("Escolha 4 para MULTIPLICAR")

controle = int(input("ESCOLHA A SUA OPERAÇÃO DESEJADA: "))
num1 = int(input("Informe um valor: "))
num2 = int(input("Informe outro valor: "))
operador = Mathe()

if num1 == 0 and num2 == 0:
    print("INFORME UM VALOR DIFERENTE DE ZERO")

elif controle == 1:
    print(Mathe.soma(num1, num2))

elif controle == 2:
    print(Mathe.subtrair(num1, num2))

elif controle == 3:
    print(Mathe.dividir(num1, num2))

elif controle == 4:
    print(Mathe.mult(num1, num2))
