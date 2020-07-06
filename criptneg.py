from Crypto.Cipher import XOR

# Escrevendo as mensagens

m1 = raw_input("Digite a mensagem para o povo: ")
m2 = raw_input("Digite a mensagem secreta: ")
cm1 = len(m1)
cm2 = len(m2)

def maior():
    m1a = m1
    m2a = m2.zfill(cm1)

#Definindo as chaves das mensagens

    k1 = raw_input("Digite a chave da mensagem para o povo: ")
    k2 = raw_input("Digite a chave da mensagem secreta: ")

#Cifrando as mensagens

    xor1 = XOR.new(k1)
    xor2 = XOR.new(k2)
    em1 = xor1.encrypt(m1a)
    print "Texto para o povo cifrado: ", em1
    em2 = xor2.encrypt(m2a)
    print "Texto secreto cifrado: ", em2

# Mesclando as mensagens

    xor3 = XOR.new(em1)
    er = xor3.encrypt(em2)
    print "Mensagem mesclada: ", er
    c = len(er)

#Definindo as chaves para decifrar as respectivas mensagens mescladas

#Chave secreta

    xor4 = XOR.new(m2a)
    kpv = xor4.encrypt(er)
    a = len(kpv)
    print "Chave secreta: ", kpv

#Chave para o povo

    xor5 = XOR.new(m1a)
    kpb = xor5.encrypt(er)
    b = len(kpb)
    print "Chave para o povo: ", kpb

#Decifrando a mensagem para o povo

    xor6 = XOR.new(kpb)
    decipher_inocent_message = xor6.encrypt(er)
    print "Mensagem para o povo: ", decipher_inocent_message

#Decifrando a mensagem secreta

    xor7 = XOR.new(kpv)
    decipher_secret_message = xor7.encrypt(er)
    print "Mensagem secreta: ", decipher_secret_message

def menor():
    m1a = m1.zfill(cm2)
    m2a = m2

#Definindo as chaves das mensagens

    k1 = raw_input("Digite a chave da mensagem para o povo: ")
    k2 = raw_input("Digite a chave da mensagem secreta: ")

#Cifrando as mensagens

    xor1 = XOR.new(k1)
    xor2 = XOR.new(k2)
    em1 = xor1.encrypt(m1a)
    print "Texto para o povo cifrado: ", em1
    em2 = xor2.encrypt(m2a)
    print "Texto secreto cifrado: ", em2

# Mesclando as mensagens

    xor3 = XOR.new(em1)
    er = xor3.encrypt(em2)
    print "Mensagem mesclada: ", er
    c = len(er)

#Definindo as chaves para decifrar as respectivas mensagens mescladas

#Chave secreta

    xor4 = XOR.new(m2a)
    kpv = xor4.encrypt(er)
    a = len(kpv)
    print "Chave secreta: ", kpv

#Chave para o povo

    xor5 = XOR.new(m1a)
    kpb = xor5.encrypt(er)
    b = len(kpb)
    print "Chave para o povo: ", kpb

#Decifrando a mensagem para o povo

    xor6 = XOR.new(kpb)
    decipher_inocent_message = xor6.encrypt(er)
    print "Mensagem para o povo: ", decipher_inocent_message

#Decifrando a mensagem secreta

    xor7 = XOR.new(kpv)
    decipher_secret_message = xor7.encrypt(er)
    print "Mensagem secreta: ", decipher_secret_message 

def igual():

    m1a = m1
    m2a = m2
#Definindo as chaves das mensagens

    k1 = raw_input("Digite a chave da mensagem para o povo: ")
    k2 = raw_input("Digite a chave da mensagem secreta: ")

#Cifrando as mensagens

    xor1 = XOR.new(k1)
    xor2 = XOR.new(k2)
    em1 = xor1.encrypt(m1a)
    print "Texto para o povo cifrado: ", em1
    em2 = xor2.encrypt(m2a)
    print "Texto secreto cifrado: ", em2

# Mesclando as mensagens

    xor3 = XOR.new(em1)
    er = xor3.encrypt(em2)
    print "Mensagem mesclada: ", er
    c = len(er)

#Definindo as chaves para decifrar as respectivas mensagens mescladas

#Chave secreta

    xor4 = XOR.new(m2a)
    kpv = xor4.encrypt(er)
    a = len(kpv)
    print "Chave secreta: ", kpv

#Chave para o povo

    xor5 = XOR.new(m1a)
    kpb = xor5.encrypt(er)
    b = len(kpb)
    print "Chave para o povo: ", kpb

#Decifrando a mensagem para o povo

    xor6 = XOR.new(kpb)
    decipher_inocent_message = xor6.encrypt(er)
    print "Mensagem para o povo: ", decipher_inocent_message

#Decifrando a mensagem secreta

    xor7 = XOR.new(kpv)
    decipher_secret_message = xor7.encrypt(er)
    print "Mensagem secreta: ", decipher_secret_message

if cm1 > cm2:
    maior()
elif cm1 < cm2:
    menor()
else:
    igual()