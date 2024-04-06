#Info
LastDateUpdated = "3/16/2024"
Dev = "D4LM"
import Functions

while True:
    def WhatOperation():
        FirstAnswer = input("What operation do you want to use?")
        if FirstAnswer == "exit":
            print("Exiting")
            exit() #Don't put any code for any reason unless it is suppose to tell of an error.
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
        if FirstAnswer == "percent to decimal":
            print("Percent to decimal mode")
            Answer3 = input("What is the number you are converting? ")
            int(Answer3)
            Answer2 = Functions.PercentToDecimal(Answer3)
            print("%" + str(Answer3) + "=" + Answer2)
        if FirstAnswer == "decimal to percent" :
            print("Decimal to percent mode")
            Answer3 = input("What is the number you are converting? (No dot only after dot, before dot will be added later...)")
            int(Answer3)
            Answer3 = Answer3 / 100
            Answer2 = Functions.DecimalToPercent(Answer3)
            print(Answer3 + "=" + Answer2 + "%")
    WhatOperation()
            