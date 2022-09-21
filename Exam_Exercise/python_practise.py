import decimal
from decimal import Decimal as D
# Beipsiele wann man decimal benützen sollte wären
# 1. Banken/Finanzen
# 2. Medizin
# 3. Teilchen Pyhisk
import fractions 
from  fractions import Fraction as F
print("First way of printing fractions:",F('1.5'))
print("second way of printing fractions:",fractions.Fraction(1.5))
#Side Notes: You can import Modules bewteen line like: import fractions <next line> from fractions import Fractions as F
print(F(D(1.5))) #Wieso mal Strings und wieso mal keine Strings
print(F(1,3)+F(1,3))
print(F(4,3))
print(F(1.5))
print("This gives out a dynamic integer number, wich python will convert to a decimal number",D(1.3))
print("This will give a static number, since we put the integer number in a string wich is an absolute number",D("1.3"))
print("Here will be 1.5 convertet to an asbolute static integer Number",F(D(1.5)))

a = 42
b = 42,5
c = "42"
d = 42.7
e = "Is this a string?"
dec = D(d)
print("Type a entspricht:",type(a))
print("Type b is:",type(b))
print("Type C is:",type(c))
print("Type d is",type(d))
print("Is Type e a String?:",isinstance(e,str))
print(int(dec))
#implizyte type converting is similar to automatic type converting performed of python 
#explicit type converting is done mannually by the user to convert a type to a specific type he requires throw defined type functions
randomDynamicList = [3,99,"sample String"] #You can edit, index, change, delete or add elements to a dictionary List
randomStaticList = (3,99,"Sample String") #You can NOT edit, change, delete or add elements to a tuble list
print(randomStaticList)
randomDynamicList.extend(["This can be a list or just a variable"]) #Extends just an element wich increases the range of the current list
#If you extend a list with a String, you have to put square brackets [] around the string, or it will just split the string in to seperate charackters
randomDynamicList.append([1,2,3]) #append adds a seperate list to the current existing list
print(randomDynamicList)

