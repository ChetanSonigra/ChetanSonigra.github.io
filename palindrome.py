from math import ceil


n = input("Please enter string or integer to check palindrome: ")

length = len(n)
i=0
if n.isalnum():
    while i <= int(length/2):
    # print(n[i],length)
        if n[i] != n[length-i-1]:
            print("This is not a palindrome")
            break
        else:
            i+=1
    #print(i)
    if i == ceil(length/2):
        print("This is a palindrome.")
else:
    print("please enter string or integer.")
        

