import math

def cifra():

   a = raw_input("Digite uma mensagem de 3 digitos: ")
   b=" ".join(str(ord(c)) for c in a) # aqui se converte caracter em valor ASCII
   c=[] #criando uma lista
   c += b.split() #dividindo a lista em pedaços
   print "Voce transmitira a mensagem: ", a
   print "Mensagem em ASCII: ", c

   m1a = input("Digite o valor de e: ")
   m1b = input("Digite o valor de n: ")
   m1=input("Digite o primeiro valor ASCII da mensagem: ")
   mc1 = m1**m1a%m1b
   
   m2=input("Digite o segundo valor ASCII da mensagem: ")
   mc2 = m2**m1a%m1b
   
   m3=input("Digite o terceiro valor ASCII da mensagem: ")
   mc3 =m3**m1a%m1b
   
   print "Mensagem a ser transmitida = ", mc1, mc2, mc3

def decifra():

   m11a =input("Digite o valor de d: ")
   m11b = input("Digite o valor de n: ")
   m11=input("Digite o primeiro valor ASCII da mensagem: ")
   mc11 = m11**m11a%m11b
   
   m22=input("Digite o segundo valor ASCII da mensagem: ")
   mc22 = m22**m11a%m11b
   
   m33=input("Digite o terceiro valor ASCII da mensagem: ")
   mc33 =m33**m11a%m11b

   w = [mc11, mc22, mc33]
   s =  "".join([chr(r) for r in w])
   print "Mensagem recebida em texto puro: ", s
   print "Mensagem recebida em ASCII: ", mc11, mc22, mc33
   
   
x = input("Escolha a opcao 1 para cifrar ou 2 para decifrar: ")

if x == 1:
   cifra()
elif x == 2:
   decifra()
else:
  print "Digite 1 ou 2!"
  x = raw_input("Escolha a opcao 1 para cifrar ou 2 para decifrar: ")