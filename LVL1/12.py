"""
* THIS PROGRAM CALCULATES FACTORIAL OF A NUMBER USING DIFFERENT METHODS
* @author gaurang mane
* @date 29.04.2026
"""
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

power = True
while power:

    print("\n---FACTORIAL OF N---\n")
#METHOD 1 - LOOPS
    while True:
        try:
            n = int(input("enter number to find factorial of: "))
            break
        except ValueError:
            print("INVALID INPUT TRY AGAIN")

    factor = 1
    for i in range(1,n+1): factor*= i
    
    print(f"\nFACTORIAL using loops    : {n}! =  {factor}")

# METHOD 2 - RECURSION OF FUNCTION
    while True:
        try:
            n = int(input("enter number to find factorial of: "))
            break
        except ValueError:
            print("INVALID INPUT TRY AGAIN")

    a = factorial(n)

    print(f"\nFACTORIAL using recursion: {n}! =  {a}")

# REPETITION
    while True:
        try:
            ask = input("\nRUN AGAIN? (Y/N): ").upper()
            if (ask == "Y" or ask == "N") : break
            else: print("ENTER Y = YES OR N = NO")
        except ValueError:
            print("INVALID INPUT TRY AGAIN")

    if(ask == "Y"): power = True
    elif (ask == "N"): power = False