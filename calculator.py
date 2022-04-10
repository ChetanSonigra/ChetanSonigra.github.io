# Calculator project :

def calculator():

    try :
        a = eval(input("Enter value 1 : "))
        opr = input("Enter the opration you want to perform : ")
        b = eval(input("Enter value 2 : "))
        if opr == "+" :
            print(a + b)
        elif opr == "-" :
            print(a-b)
        elif opr == "*":
            print(a*b)
        elif opr == "/":
            print(a/b)
        elif opr == "**" :
            print(a**b)
        else :
            print(f"invalid operator '{opr}' found, Valid operator are (+,-,*,/,**)",)
    except NameError :
        print("please add numbers")
        calculator()


calculator()

    
    
