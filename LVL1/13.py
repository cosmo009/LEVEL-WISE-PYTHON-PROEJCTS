"""
* THIS PROGRAM CHECKS WHETHER A NUMBER IS A PRIME NUMBER OR NOT
* @author gaurang mane
* @date 29.04.2026
"""
def isPrime(n):
    if n == 0 or n == 1 or n==2: return True
    
    for i in range (2,n):
        if (n%i==0): 
            return False
        
    return True

power = True
while power:

    print("\n---PRIME CHECK OF N---\n")
    while True:
        try:
            n = int(input("enter a number : "))
            break
        except ValueError:
            print("INVALID INPUT TRY AGAIN")

    a = bool(isPrime(n))
    print(a)
    if a: print(f"{n} is Prime.")
    else: print(f"{n} is NOT Prime")

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