"""
* THIS PROGRAM CHECKS WHETHER A NUMBER IS A PALINDROME OR NOT
* @author gaurang mane
* @date 22.05.2026
"""
def isPalindrome(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
    
power = True
while power:
    print("\n---PALINDROME CHECKER---")

    n = input("Enter a number: ")
    ans = isPalindrome(n)
    print(f"Palindrome : {ans}")


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