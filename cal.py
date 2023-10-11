import os
import math


#all functions 
def process(num1,ac, num2):
    num1 =float(num1)
    num2 = float(num2)
    if ac == "+":
        print("= ",num1 + num2)
    elif ac =="-":
        print("= ",num1 - num2)
    elif ac =="/":
        if num2 == 0:
            print("Error")
        else:
            print("= ",num1/num2)
    elif ac =="*":
        print("= ",num1*num2)
    else:
        print("Invalid Input")




def sqar_manu():
    os.system('cls')
    print("-------Square Root-------")
    num = int(input("Enter the number: "))
    sq = math.sqrt(num)
    print("The square root of ", num , " is ", round(sq,3))
    while(True):
            ty = input("Want to try again? Y/N: ")
            if ty.upper() == "Y":
                os.system('cls')
                sqar_manu()
            elif ty.upper() =="N":
                os.system('cls')
                adv_math_menu()
            else:
                os.system("cls")
                print("Try again: ")
    

 
        
def exp_menu():
    os.system('cls')
    print("-------EXPONENTIATION-------")
    num =(input("Enter a number and also the expoenent(With space):  "))
    num_1 , num_2  = num.split()

    num_1 = int(float(num_1))
    num_2 = int(float(num_2))   
    
    ans = pow(num_1,num_2)
    print("The expoent of ",num_1 ,"^",num_2,"is ", ans)
    while(True):
        ty = input("Want to try again? Y/N: ")
        if ty.upper() == "Y":
            os.system('cls')
            exp_menu()
        elif ty.upper() =="N":
            os.system('cls')
            adv_math_menu()
        else:
            os.system("cls")
            print("Try again: ")  

def trigomenu():
    os.system('cls')
    print("-------TRIGONOMETRIC FUNCTIONS-------")
    num = (input("Enter the trigo function and number(SIN, COS, TAN): "))
    trigo , num1 = num.split()

    trigo = str(trigo.upper())
    num1 = float(num1)

    if trigo == "SIN":
        print("SIN ",num1," = ",math.sin(num1))
    elif trigo == "COS":
        print("COS  ",num1," = ",math.cos(num1))
    elif trigo == "TAN":
        print("TAN ",num1," = ",math.tan(num1))
    
    while(True):
        ty = input("Want to try again? Y/N: ")
        if ty.upper() == "Y":
            os.system('cls')
            trigomenu()
        elif ty.upper() =="N":
            os.system('cls')
            adv_math_menu()
        else:
            os.system("cls")
            print("Try again: ")  
    
def logmenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-------LOGARITHMIC FUNCTIONS-------")
    
    while True:
        try:
            num = float(input("Enter a positive number: "))
            if num > 0:
                print(f"log({num}) = {math.log10(num):.9f}")
            else:
                print("Only positive numbers are allowed.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        ty = input("Want to try again? Y/N: ")
        if ty.upper() == "Y":
            os.system('cls')
        elif ty.upper() == "N":
            os.system('cls')
          
            return
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid choice. Try again.")




def facmenu():
    os.system('cls')
    print("-------FACTORIAL-------")
    num = float(input("Enter number: "))

    if num < 0:
        print("Only positve number")
    else:
        print("factorial ",num,"=", math.factorial(num))
    while(True):
        ty = input("Want to try again? Y/N: ")
        if ty.upper() == "Y":
            os.system('cls')
            facmenu()
        elif ty.upper() =="N":
            os.system('cls')
            adv_math_menu()
        else:
            os.system("cls")
            print("Try again: ")          

def basic_op_menu():
    pi = math.pi
    print("-------BASIC OPERATION-------")
    while True:
        user_input = input("Enter 2 numbers and the operator (Include Space): ")
        num1, operator, num2 = user_input.split() 
        try:
            if num1 == "pi":
                num1 = pi
            else:
                num1 = float(num1)
            if num2 == "pi":
                num2 = pi
            else:
                num2 = float(num2)

            result = process(num1, operator, num2)
    

            while True:
                ty = input("Want to try again? Y/N: ")
                if ty.upper() == "Y":
                    os.system('cls')
                    basic_op_menu()
                elif ty.upper() == "N":
                    os.system('cls')
                    main()
                else:
                    print("Invalid input. Try again: ")
        except ValueError:
            os.system('cls')
            print("Invalid input. Please enter valid numbers and operator.")

def adv_math_menu():
     os.system('cls')
     print("-------ADVANCE MATHEMATICAL FUNCTIONS-------")
     print("A - Square Root \nB - Exponentiation \nC - Trigonometric Functions(SIN,COS,TAN) \nD - Logarithmic Functions \nE - Factorial \nF - Main Menu ")
     choice = input("Enter the operations you want: ")
    
     if choice.upper() == 'A':
         sqar_manu()
     elif choice.upper() =='B':
         exp_menu()
     elif choice.upper() =='C':
         trigomenu()
     elif choice.upper() =='D':
         logmenu()
     elif choice.upper() =='E':
         facmenu()
     elif choice.upper() =='F':
         os.system('cls')
         main()
     else:
        os.system("cls")
        print("Try again: ")



def main():

    while(True):
        print("------Scientific Calculator-----")
        print("A - Basic Operation \nB - Advanced Mathematical Functions \nC - Exit")
        choice = input("Enter the operations you want: ")

        if choice.upper() == 'A':
            os.system("cls")
            basic_op_menu()
        elif choice.upper() =='B':
            adv_math_menu()
        elif choice.upper() =='C':
            os.system('cls')
            print("Exit Succesful")
            break
        else:
            os.system("cls")
            print("Try again: ")






main()
