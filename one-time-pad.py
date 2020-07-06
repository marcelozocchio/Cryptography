# -*- coding: cp1252 -*-

import random
from Crypto.Cipher import XOR

def cifra():
    caracter = "abcçdefghijklmnopqrstuvwxyzABCÇDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()§-_+=§{}[]|\/:;<>.,"
    mensagem = raw_input("Digite aqui a mensagem a ser cifrada: ")
    tamanho_da_senha = len(mensagem)
    if (tamanho_da_senha < 0):
        print "Erro: valor negativo!"
    elif (tamanho_da_senha == 0):
        print "Erro: Tem que ter pelo menos 1 caracter!"
    else:
        senha = ""
        while len(senha) != tamanho_da_senha:
            senha = senha+random.choice(caracter)
        print "Senha gerada: ", senha

    xor1 = XOR.new(senha)
    mensagem_cifrada = xor1.encrypt(mensagem)
    print mensagem_cifrada.encode('hex')

def decifra():
    mensagem = raw_input("Digite aqui a mensagem a ser decifrada: ")
    mensagem1 = mensagem.decode('hex')
    senha = raw_input("Digite a senha: ")
    xor2 = XOR.new(senha)
    mensagem_decifrada = xor2.decrypt(mensagem1)
    print mensagem_decifrada

def menu():
    a = raw_input("Digite 1 para cifrar ou 2 para decifrar: ")
    if a == '1':
        cifra()
    elif a =='2':
        decifra()
    else:
        print "Escolha certo!"
        menu()
menu()