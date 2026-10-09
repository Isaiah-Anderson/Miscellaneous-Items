import math
Menu = " 1. Add\n 2. Subtract\n 3. Divide\n 4. Multiply\n"
print("========== CALCULATOR ==========")
print(Menu)
Selection = input("Select your function: ")


if Selection == "1":
    InputOne = float(input("Select First Number: "))
    InputTwo = float(input("Select Second Number: "))
    AdditionOne = float(InputOne + InputTwo)
    print(AdditionOne)

elif Selection == "2":
    InputOne = float(input("Select First Number: "))
    InputTwo = float(input("Select Second Number: "))
    AdditionOne = float(InputOne - InputTwo)
    print(AdditionOne)

elif Selection == "3":
    InputOne = float(input("Select First Number: "))
    InputTwo = float(input("Select Second Number: "))
    AdditionOne = float(InputOne / InputTwo)
    print(AdditionOne)

elif Selection == "4":
    InputOne = float(input("Select First Number: "))
    InputTwo = float(input("Select Second Number: "))
    AdditionOne = float(InputOne * InputTwo)
    print(AdditionOne)

else:
    print("Goodbye")
