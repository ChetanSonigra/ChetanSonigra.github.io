
def factorial(n):
        if n<2:
            return 1
        else:
            return n*factorial(n-1)

try:
    n = int(input("Please enter integer to find factorial: "))
except Exception as err:
    print(f"Not a valid input : {err}")
else:
    result = factorial(n)
    print(result)


