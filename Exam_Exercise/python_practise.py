'''import fractions
print(fractions.Fraction(1.5))'''

import fractions 
import decimal
from fractions import Fraction as F
from decimal import Decimal as D
'''
print(F(D('1.3')))
print(F(D('1.5')))
print(D('1.3')) 
#print(D(1.3)) 
print(F(1,3) + F(1,3))
print(F(1.3) + F(1.3))
print(F('1.3') + F('1.3'))
print(F("2.6"))


i = 42
print(type(i))
a = '''

X = [3, 0, "Lid"]
print(X[2])
y = [0, 2, (3, 4), [1,3], "Lid" ]
print(y[2])
S = (2, 0, 1, (3, 3))
print(S[3])
text = "01234567"
text = "Hello"
print(text[0:4])

upperTest = ("hello world").upper() #Upper writes the string all in big capitals
print(upperTest)

import time 
n = 1000
start_time = time.time()
liste = []
for i in range(n):
    liste = liste + [i * 2]

print(time.time() - start_time)
print(time.time())

