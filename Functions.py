#Addition
def Addition(a,b):
    Answer = a + b
    return Answer

#Subtraction
def Subtraction(a,b):
    Answer = a - b
    return Answer

#Multiplication
def Multiplication(a,b):
    Answer = a * b
    return Answer

#Division
def Division(a,b):
    Answer = a/b
    return Answer

#Exponent
def Exponent(a,b):
    Answer = a**b
    return Answer

#Roots
def Roots(a,b):
    if a >= 0:
        Answer = a**(1/b)
        return Answer
    if a < 0:
        Answer = -(-a)**(1/b)
        return Answer
print(Roots(4,2))