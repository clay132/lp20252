#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
prv= float(input("qual é o valor da prestação vencida :"))
juro= float(input("qual é o valor do juros :"))
per_atraso= float (input("quanto tempo de atraso em mes :")) 
print ("o valor da prestaçao atarada é", prv)
print ("o periodo de atraso :", per_atraso)
print ("a taxa que sera cobrada é:", juro)
valor_final= prv +(((juro/100)*prv)*per_atraso)
print ("o valor total sera :",valor_final)