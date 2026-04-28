"""
* @author gaurang mane
"""
print("\n---ENTER THREE NUMBERS---")
#there are several methods to find max among three numbers
#here are a few of them

while True:
    try:
        a = float(input("\nEnter first number: "))
        break
    except ValueError:
        print("Invalid Numbers. Try again...")

while True:
    try:
        b = float(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid Numbers. Try again...")

while True:
    try:
        c = float(input("Enter third number: "))
        break
    except ValueError:
        print("Invalid Numbers. Try again...")
    
#using ternary within ternary
max_ = (a if a>c else c) if a>b else (b if b>c else c)
print(f"\nMax among {a}, {b} and {c} is {max_}.")



#taking multiple numbers input once altogether
while True:
    try:
        numbers = list((str(input("\nEnter numbers tofind max from: "))).split(" "))
        break
    except ValueError:
        print("Invalid Numbers. Try again...")


max_ = max(numbers)
print(f"\nMax among numbers is {max_}.")


#or the classic method of if else statements
#this is ntg but expanding the nested ternary i used in the first method. so i am just skipping it