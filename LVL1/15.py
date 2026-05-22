"""
* THIS PROGRAM REVERSES A NUMBER
* @author gaurang mane
* @date 22.05.2026
"""
def reverseNumber(n):
    return int(str(n)[::-1])

power = True
while power:
    print("\n---NUMBER REVERSAL---")

    while True:
        n = input("Enter a number: ")
        if n.isdigit():
            n_int = int(n)
            break
        else:
            print("Please enter a valid integer.")

    ans = reverseNumber(n_int)
    print(f"Reversed : {ans}")

    while True:
        ask = input("\nRUN AGAIN? (Y/N): ").upper()
        if (ask == "Y" or ask == "N"):
            break
        else:
            print("ENTER Y = YES OR N = NO")

    if ask == "Y":power = True  
    elif ask == "N":power = False           

    """
    THERE IS SOME ERROR IN THE PROGRAM AND I WILL FIX IT LATER
    """                                                                       