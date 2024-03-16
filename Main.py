#Info
LastDateUpdated = "3/16/2024"
Dev = "D4LM"
import Functions

while True:
    def WhatOperation():
        FirstAnswer = input("What operation do you want to use?")
        if FirstAnswer == "exit":
            print("Exiting")
            exit() #Don't put any code for any reason unless it is suppose to tell of a problem.
        if FirstAnswer == "info":
            print("Developer: " + Dev)
            print("Last date updated: " + LastDateUpdated)
        if FirstAnswer == "+":
            print("Addition mode")
            y = int(input("What is the first number?"))
            z = int(input("What is the second number?"))
            SecondAnswer = str(Functions.Addition(y,z))
            print(str(y) + "+" + str(z) + "=" + SecondAnswer)
        if FirstAnswer == "-":
            print("Subtraction mode")
            y = int(input("What is the first number?"))
            z = int(input("What is the second number?"))
            SecondAnswer = str(Functions.Subtraction(y,z))
            print(str(y) + "-" + str(z) + "=" + SecondAnswer)
        if FirstAnswer == "*":
            print("Multiplication mode")
            y = int(input("What is the first number?"))
            z = int(input("What is the second number?"))
            SecondAnswer = str(Functions.Multiplication(y,z))
            print(str(y) + "*" + str(z) + "=" + SecondAnswer)
        if FirstAnswer == "/":
            print("Division mode")
            y = int(input("What is the first number?"))
            z = int(input("What is the second number?"))
            SecondAnswer = str(Functions.Division(y,z))
            print(str(y) + "/" + str(z) + "=" + SecondAnswer)
        if FirstAnswer == "^":
            print("Exponent mode")
            y = int(input("What is the first number?"))
            z = int(input("What is the second number?"))
            SecondAnswer = str(Functions.Exponent(y,z))
            print(str(y) + "^" + str(z) + "=" + SecondAnswer)
        if FirstAnswer == "root":
            print("Root mode")
            y = int(input("What is the first number?"))
            z = int(input("What is the second number?"))
            SecondAnswer = str(Functions.Roots(y,z))
            print(SecondAnswer)
    WhatOperation()
            