#1. Faça um programa que imprima o seu nome.
def q1():
    cabecalho('QUESTÃO 1')
    print('João Paulo')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q2():
    cabecalho('QUESTÃO 2')
    print(30*27)
#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q3 ():
nume1 = 5
nume2 = 8
nume3= 12
soma = nume2+nume3+nume1
aritmetica = soma // 3
print ("a media aritmetica dos numeros 5,8,12 é:",aritmetica )
#4.Faça um programa que leia e imprima um número inteiro.
def q4():
numero = int(input("escreva um núnumero inteiro:"))
print (numero)
#5. Faça um programa que leia dois números reais e os imprima.
def q5():
nur1 = float(input("escreva um numero reais:"))
nur2 = float (input("escreva um numero reais :"))
print("o primeiro numero reais é:",nur1,"o segundo numero é:", nur2)
Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q6():
numero = int(input ("digite um numero inteiro:"))
sucessor= numero + 1
antecessor = numero - 1
print ("sucessor:", sucessor,"antecessor:",antecessor)
#Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q7():
nome =(input("qual é o seu nome: "))
ende= (input ("qual é o seu endereço: "))
telef= (input ("digite o seu telefone: "))
print ("o nome do cliente é:",nome,"o endereço do é:",ende,"telefone:",telef)
# Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q8():
print("os numeros que vc escrevera sera subtraido entre eles ")
nmr1= int(input ("escreva um numero inteiro:"))
nmr2=int(input("escreva um numero inteiro:"))
print(nmr1- nmr2)
#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q9():
nmr= float(input("escreva um numero real:"))
resultado = nmr /4 
print ("1/4 de ",nmr,"é:", resultado)
# Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
numero1= float (input ("digita o primeiro numero:"))
numero2= float(input("digita o sengundo numero:"))
numero3= float (input("digita o terceiro numero:"))
soma= numero1+ numero2+numero3
resultado = soma/3
print ("a media aritmetica dos numeros:",numero1,numero2,numero3, "é:",resultado)
#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
def q18():
t=int(input("qual  foi o tempo decorrido na viagem: "))
v = int (input("qual é a velocidade media :"))
D = (t*v)
L= (D/12)
print (D)
print(L)
#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
def q19():
prv= float(input("qual é o valor da prestação vencida :"))
juro= float(input("qual é o valor do juros :"))
per_atraso= float (input("quanto tempo de atraso em mes :")) 
print ("o valor da prestaçao atarada é", prv)
print ("o periodo de atraso :", per_atraso)
print ("a taxa que sera cobrada é:", juro)
valor_final= prv +(((juro/100)*prv)*per_atraso)
print ("o valor total sera :",valor_final)
#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.
def q20():
rs= float(input("digite o valor em R$:"))
cota= float(input("qual é o valor da cotaçao do dolar:"))
dolar= (rs * cota)
print(dolar)

