lista= ["maça","melancia","banana","melão","uva"]
# 1. Peça o nome do usuário e imprima "Olá, <nome>"
def q1():
 nm=input("escreva o seu nome")
 print ("olá",nome)
# 2. Peça a idade do usuário e imprima "Você tem <idade> anos"
def q2():
 idade=input("digita idade: ")
 print(idade,"anos")
# 3. Peça dois números e imprima a soma deles
def q3():
 numero_1=int(input("digita um numero: "))
 numero_2=int(input("digita um numero"))
 print(numero_2 + numero_1)
# 4. Peça dois números e imprima a média
def q4():
    soma=0
    for i in range(2):
     numero=int(input("digita um numero: "))
     soma+= numero
    media= soma/2
    print(media)   
# 5. Peça três números e use sum() para somá-los
def q5():
    
  numero=[int(input("digita um numero "))for i in range(3)]
  print(sum(numero))
     
# 6. Peça três números e use len() para mostrar quantos números foram digitados
def q6():
 numero=[int(input(f"digita {i+1}° numero: "))for i in range(3)]
 print("a quantidade de numero digitados são",len(numero))

# 7. Pergunte o nome e a idade do usuário e mostre o tipo de cada variável usando type()
def q7():
    nome= input ("escreva nome")
    idade= int(input("digita idade: "))
    print(type(nome), nome)
    print(type(idade),idade)
# 8. Crie uma função que recebe o nome do usuário e imprime "Bem-vindo, <nome>"
def q8 ():
    nome=input("escreva o seu nome: ")
    print("bem vindo", nome)
# 9. Crie uma função que soma dois números
def q9():
    
    nm1 = int(input("Digite o primeiro número: "))
    nm2 = int(input("Digite o segundo número: "))
    
    soma = nm1 + nm2
    print("A soma dos números é:", soma)



# 10. Crie uma função que retorna o maior número entre dois números
def q10():
    nm=[int(input(f"digita {i +1} numero: ")) for i in range(2)]
    print(max(nm))
# 11. Crie uma lista de 5 frutas e imprima cada uma usando for
def q11():
 global lista
 for i, fruta in  enumerate (lista, start=1):
  print(i,fruta)
  
 
# 12. Adicione uma fruta na lista criada no exercício anterior
def q12():
 global lista
 lista.append("laranja")#esse .append adiciona coisas dentro de lista 
 for i,fruta in  enumerate (lista,start=1):
  print(i,fruta)
 
# 13. Remova a última fruta da lista
def q13():
 global lista
 lista.pop()
 for i, fruta in enumerate(lista,start=1) :
  print(i,fruta)
  return lista
 
# 14. Mostre quantos itens existem na lista usando len()
def q14():
 lista=q13()
 print(len(lista)) # "len()mostra a quantidade de coisas que ta na lista"
# 15. Crie uma tupla com 3 cores e imprima a primeira cor
def q15():
    cores=("vermelho","azul","amarelo")
    print(cores[0])
    return cores
# 16. Tente mudar o primeiro item da tupla (veja o erro)
def q16():
    cores=q15()
    cores[0]=("verde")

# 17. Crie um dicionário com "nome", "idade" e "curso" e imprima o nome
def q17():
 aluno={
  "nome": "clay",
  "idade":18,
  "curso":"rede computadores"
  }

 print(aluno["nome"])
 return aluno
 
# 18. Adicione uma nova chave "cidade" ao dicionário
def q18():
 aluno= q17()
 aluno["cidade"]="cuiaba"
 print(aluno["cidade"])
 return aluno
# 19. Altere o valor da idade no dicionário
def q19():
 aluno=q18()
 aluno["idade"]=19
 print(aluno["idade"])

# 20. Crie um conjunto com 5 números, alguns repetidos, e veja quais sobraram
def q20():
 conjunto={1,2,2,3,4,5}
 print(conjunto)

# 21. Pergunte ao usuário números separados por espiaço, transforme em lista e use sum()
def q21():
 nm=input("digita numeros separados por espaço: ")
 nm2= nm.split() # "aqui o split trasforma string em lista"
 nm3= [int(item) for item in nm2]
 print(sum(nm3))
 
# 22. Crie um loop for que imprime números de 0 a 9
def q22():
 for i in range(10):
   print(i)
# 23. Crie um loop while que imprime números de 0 a 9
def q23():
   n=0
   while n<10:
    print(n)
    n+=1

# 24. Crie um loop while que pede um número até o usuário digitar 0
def q24():
    while True:
      numero_digitar=int(input("digita um numero: "))
      if numero_digitar==0:
        print("numero certo")
        break
      else:
        print(numero_digitar)
     
# 25. Crie uma função que recebe uma lista de números e retorna a soma
def q25 (soma):
  return sum(soma)
  
  
# 26. Crie uma função que recebe uma lista e retorna a média
def q26(lista):
   soma=sum(lista)
   quantidade=len(lista)
   media= soma/quantidade
   return media

# 27. Crie uma função que recebe um número e retorna True se for par, False se for ímpar
def q27(numero):
  if numero%2==0:
   return True
  else:
   return False
# 28. Crie uma função que recebe um número e retorna o fatorial (use math.factorial)
def q28(numero):
  import math 
  resultado=math.factorial(numero)
  return resultado

# 29. Crie uma função que recebe o raio e retorna a área do círculo (use math.pi)
def q29(raio):
  import math
  area=math.pi*(raio**2)
  return area
# 30. Abra um arquivo e escreva uma linha de texto

def q30(arquivo,texto):
  with open(arquivo,"w") as arq:#é so colocar *a* no lugar do w pra escreve sem apagar
    arq.write(texto)
    print(f"texto: {texto}  o arquivo é  {arquivo}")
# 31. Abra o mesmo arquivo e adicione mais uma linha sem apagar o que já tem
def q31(arquivo,texto):
  with open(arquivo,"a") as arq:#é so colocar *a* no lugar do w pra escreve sem apagar
    arq.write(texto)
    print(f"texto: {texto}  o arquivo é  {arquivo}")
# 32. Abra o arquivo e leia todo o conteúdo
def q32(arquivo):
  with open(arquivo,"r")as arq:
    conteudo=arq.read()
  print(f"o arquivo é {arquivo}:\n{conteudo}")
  return conteudo
# 33. Abra o arquivo e leia linha por linha usando loop
def q33(arquivo):
   conteudo= q32(arquivo)
   linhas= conteudo.splitlines()
   for i,linha in enumerate (linhas, start=1):
     print(f"linha{i}:{linha}")

# 34. Crie uma lista vazia e adicione 5 números usando append
def q34():
  listal=[]
  listal.append(5)
  listal.append(6)
  listal.append(7)
  listal.append(8)
  listal.append(9)
  print(listal)

  
# 35. Crie uma lista com números de 1 a 10 usando range()
def q35():
  
 listal= list(range(1, 11))
 print(listal)
# 36. Use um for para imprimir os quadrados dos números de 1 a 10
def q36():
  for numero in range(1, 11):
        print(numero**2)
# 37. Crie um loop que percorre uma lista e imprime somente os números pares
def q37():
  lista=[2,3,4,5,6,7,8,9,10] 
  for numero in lista:
    if numero % 2==0:
     print(numero)
    

# 38. Crie uma lista com nomes e use len() para imprimir quantos nomes tem
def q38():
 lista=["clay","marjorie", "julson"]
 print(len(lista))
# 39. Crie um dicionário de alunos e notas e imprima a média das notas
def q39():
 dicionario={
 "aluno":input(""),
 "nota_1":int(input("nota 1:")),
 "nota_2": int(input("nota 2:"))

 }
 media= ( dicionario["nota_1"] +dicionario[ "nota_2"]) /2
 print(media)
# 40. Crie um conjunto com letras de uma palavra e veja quantas letras únicas existem
def q40():
 palavra=input("escreva uma palavra: ")
 conjunto=set(palavra)
 print(len(conjunto)) 

# 41. Crie uma função que recebe uma lista de palavras e retorna a palavra mais longa
def q41():
 palavra_1= input("escreva um palavra :")
 palavra_2= input("escreva um palavra :")
 verificar_1=len(palavra_1)
 verificar_2=len(palavra_2)
 if verificar_1 > verificar_2:
  print("a primeira palavra é maior ")
 else:
  print("a segunda e maior ")
  
# 42. Crie uma função que recebe uma lista de números e retorna o menor número
def q42(numero):
 print(numero)
 numero_menor=min(numero)
 return numero_menor
# 43. Crie um loop while que pede números até a soma passar de 100
# 44. Crie uma função que recebe um número e retorna True se for primo
# 45. Peça 5 números do usuário e armazene em uma lista usando loop
# 46. Use for para imprimir os índices de uma lista (use range(len(lista)))
# 47. Crie um programa que lê uma lista de números e imprime a soma e a média
# 48. Crie um dicionário com nomes de pessoas e idades, e imprima só as pessoas maiores de 18
# 49. Crie um arquivo "numeros.txt" e salve 10 números dentro, um por linha
# 50. Abra o arquivo "numeros.txt" e calcule a soma de todos os números
nn=[1,2,3,4,5]
print(q42(nn))