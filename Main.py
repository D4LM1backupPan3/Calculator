#Info
LastDateUpdated = 3/14/2024
import Functions

while True:
    def WhatOperation():
        FirstAnswer = input("What operation do you want to use?")
        if FirstAnswer == "exit":
            print("Exiting")
            exit()
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
    WhatOperation()
            