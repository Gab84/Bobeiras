def soma (n1, n2):
    return n1+n2 

def subtracao (n1, n2):
    return n1 - n2

def multiplicacao (n1, n2):
    return n1 * n2

def divisao (n1, n2):
    return n1 / n2

def sobra (n1, n2):
    return n1 % n2

"""def soma (n1, n2):
    return n1 +n2

def soma (n1, n2):
    return n1 +n2

def soma (n1, n2):
    return n1 +n2

def soma (n1, n2):
    return n1 +n2
"""


while True :
    print(' 1 = soma \n 2 = subtração \n 3 = multiplicação \n 4 = divisão \n 5 = Sobra ')
    opcao = int(input('Escolha oque deseja : '))
    
    if opcao == 0 :
        
        print('numero invalo')
    if opcao == 1:
        n1=float(input('digite o numero 1 = '))
        n2=float(input('digite o numero 2 = '))
        resultado = soma(n1,n2)
        print(f'o resultado da soma é {resultado}')        
    if opcao == 2:
        n1=float(input('digite o numero 1 = '))
        n2=float(input('digite o numero 2 = '))
        resultado = subtracao (n1, n2)
        print(f'o resultado da soma é {resultado}')        


""""""

#progressão aritimetrica
a_n = int(print('digite o valor que quer calcular'))
a_1 = a_n
Nq = int(print('Digite a posição que você quer descobrir'))
Raz = int(print('Digite o valor da razão (valor que é somado na progressão)'))
Calculo = a_1 + (Nq - 1)*Raz
print(Calculo)
#

