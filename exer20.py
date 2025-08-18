#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.
rs= float(input("digite o valor em R$:"))
cota= float(input("qual é o valor da cotaçao do dolar:"))
dolar= (rs * cota)
print(dolar)