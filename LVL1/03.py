"""
* @author gaurang mane
"""
success = False
while(not success):
    try:
        num = int(input("Enter a number: "))
        success = True
    except ValueError:
        print("That's not a valid number. Please try again.")

if (num%2==0):
    print(f"\n{num} is even.")
else: print(f"\n{num} is odd.")