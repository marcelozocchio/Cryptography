def fatorar ():
 
   resto = m
 
   if( m <= 0 ):
       print "Numero invalido!"
 
   else:
       divisor = 2
       fatores = {}
       soma_divisores = 1
 
       #fatorar o numero
       while resto >= 0 and divisor <= resto:
           if( resto % divisor == 0 ):
               #salvar o numero de vezes que cada fator aparece (expoentes)
               if( fatores.has_key(divisor) ):
                   fatores[divisor] += 1
               else:
                   fatores[divisor] = 1
 
               resto = resto // divisor
           else:
               divisor += 1
   print fatores

def euclides():
   
   a=e
   b=m
   dividendo = a
   divisor = b
   restos = []
  
   while dividendo%divisor > 0:
       c=dividendo%divisor
       restos+=[c]
       dividendo=divisor
       divisor = c
   #print "MDC = ", divisor
   #print "Restos da divisao = ", restos

def euclides_estendido():
   resposta = {}
   x = {}
   y = {}
   x[0] = 1
   x[1] = 0
   y[0] = 0
   y[1] = 1
   a1 = e
   a2 = m
   while a1%a2 <> 0:
              quociente1 = a1/a2
              temp1 = a1
              a1 = a2
              a2 = temp1%a2
              x1 = x[0]-(x[1]*quociente1)
              y1 = y[0]-(y[1]*quociente1)
              x[0] = x[1]
              x[1] = x1
              y[0] = y[1]
              y[1] = y1
   resposta[0] = x[1]
   resposta[1] = y[1]
   resposta[2] = a2
   #print "Valor do inverso modular: ", resposta[0]
   print "Sua chave privada sera composta por:"
   print "n = ", n 
   print "d = ", resposta[0]
   if resposta[0] < 0:
      print "Chave com valor negativo; tente outra combinacao"

p=input("Digite um numero primo maior ou igual a 17: ")
q=input("Digite outro numero primo menor que o anterior: ")
n=p*q
m=(p-1)*(q-1) 
   
fatorar()

e = input("Digite um numero primo diferente daqueles que estao antes dos dois pontos: ")
print "Sua chave publica sera composta por:" 
print "n = ", n 
print "e = ", e

euclides()
euclides_estendido()