from Crypto.Hash import SHA512
from Crypto.Hash import SHA384
from Crypto.Hash import SHA256
from Crypto.Hash import SHA224
from Crypto.Hash import RIPEMD
from Crypto.Hash import MD5
from Crypto.Hash import MD4
from Crypto.Hash import MD2
import whirlpool
import hashlib

a = raw_input("Digite uma string: ")
b = SHA512.new(a).hexdigest()
c = SHA384.new(a).hexdigest()
d = SHA256.new(a).hexdigest()
e = SHA224.new(a).hexdigest()
f = RIPEMD.new(a).hexdigest()
g = MD5.new(a).hexdigest()
h = MD4.new(a).hexdigest()
i = MD2.new(a).hexdigest()
j = whirlpool.new(a).hexdigest()
l = hashlib.sha1(a).hexdigest() 
print "SHA512 = ", b
print "SHA384 = ", c
print "SHA256 = ", d
print "SHA224 = ", e
print "RIPEMD160 = ", f
print "MD5 = ", g
print "MD4 = ", h
print "MD2 = ", i
print "Whirlpool = ", j
print "SHA1 = ", l
