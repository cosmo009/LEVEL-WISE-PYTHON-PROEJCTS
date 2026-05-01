"""
* THIS IS A SIMPLE PASSWORD VALIDATOR
* It enforces that the password created should contain the following:
    1. minimum of 8 character
    2. Atleast 1 uppercase and 1 lowercase letter
    3. Atleast 1 digit
    4. Atleast 1 special character
    5. No spaces
* @author gaurang mane
* @date 29.04.2026
"""
#returns bool,error_count and errors
def password_validation(string):
    valid = False
    error = " "    
    count = 0

    cond1 = False
    if len(string)>=8: cond1 = True
    else: 
        count+=1
        error += f"{str(count)}. Password is too short.\n "

    cond21 = False
    cond22 = False
    cond3 = False
    cond4 = False
    cond5 = True
    for i in range(len(string)):
        if(65<=ord(string[i])<=90): 
            cond21 = True
        elif(i==(len(string)-1) and (not cond21)): 
            count+=1
            error += f"{str(count)}. Password should contain atleast 1 uppercase letter\n "

        if(97<=ord(string[i])<=122 ): 
            cond22 = True
        elif(i==(len(string)-1) and (not cond22) ): 
            count+=1
            error += f"{str(count)}. Password should contain atleast 1 lowercase letter.\n "

        if(48<=ord(string[i])<=57): 
            cond3 = True
        elif(i==(len(string)-1) and (not cond3)): 
            count+=1
            error += f"{str(count)}. Password should contain atleast 1 digit.\n "

        if(string[i] in "!@#$%^&*_~"): 
            cond4 = True
        elif(i==(len(string)-1) and (not cond4)): 
            count+=1
            error += f"{str(count)}. Password should contain atleast 1 special character.\n "

        if(string[i]==" "): 
            cond5 = False
        elif(i==(len(string)-1) and (not cond5)): 
            count+=1
            error += f"{str(count)}. Password should not contain spaces.\n "

    if(cond1 and cond21 and cond22 and cond3 and cond4 and cond5): valid = True

    return valid,error




power = True
while power:
    print("\n---PASSWORD VALIDATOR---")

    str1 = input("Enter your password: ")
    valid,error = password_validation(str1)
    print(f"Validity = {valid}")
    if (not valid): print(f"ERROR:\n{error}")

    while True:
        try:
            ask = input("\nRUN AGAIN? (Y/N): ").upper()
            if (ask == "Y" or ask == "N") : break
            else: print("ENTER Y = YES OR N = NO")
        except ValueError:
            print("INVALID INPUT TRY AGAIN")

    if(ask == "Y"): power = True
    elif (ask == "N"): power = False