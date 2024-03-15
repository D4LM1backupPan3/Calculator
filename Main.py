#Info
LastDateUpdated = 3/14/2024
import Functions

while True:
    def WhatOperation():
        FirstAnswer = input("What operation do you want to use?")
        if FirstAnswer == "+":
            print("Addition mode")
            y = int(input("What is the first number?"))
            z = int(input("What is the second number?"))
            print("Answer is...")
            print(Functions.Addition(y,z))
    WhatOperation()
            