#As of now using a constant value to check the password and username
USERNAME = "JohnDoe"
PASSWORD  ="helloWorld@1234"

def isUserValid(username):
    return True if (username==USERNAME) else  False

def isPwrdValid(password):
    return True if (password==PASSWORD) else  False


"""
* THIS IS A SIMPLE USER LOGIN SYSTEM
* which validates a user's login by checking the password and username using functions
* @author gaurang mane
* @date 29.04.2026
"""

power = True
while power:
    print("\n---SIMPLE USER LOGIN SYSTEM---")

    inputUser     = input("Username:  ")
    inputPassword = input("Password: ")
    
    if(isUserValid(inputUser) and isPwrdValid(inputPassword)):
        print(f"\nWelcome, {USERNAME}!")
    elif(not(isUserValid(inputUser))):
        print(f"\nInvalid Username. Try again.")
    else: 
        print(f"\nInvalid login credentials.")


    while True:
        try:
            ask = input("\nRUN AGAIN? (Y/N): ").upper()
            if (ask == "Y" or ask == "N") : break
            else: print("ENTER Y = YES OR N = NO")
        except ValueError:
            print("INVALID INPUT TRY AGAIN")

    if(ask == "Y"): power = True
    elif (ask == "N"): power = False