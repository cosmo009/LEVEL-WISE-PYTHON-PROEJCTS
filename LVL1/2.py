
#MUCH SIMPLER BASIC CALCII
power = True
while(power):
    ask = True
    success1 = False
    while(not success1):
        try:
            num1 = float(input("\nEnter 1st number: "))
            success1 = True
        except ValueError:
            print("INVALID INPUT. TRY AGAIN")

    success2 = False
    while(not success2):
        try:
            num2 = float(input("Enter 2nd number: "))
            success2 = True
        except ValueError:
            print("INVALID INPUT. TRY AGAIN")
            

    success3 = False
    while(not success3):
        op = str(input("\nEnter operator (ADD +)(SUB -)(DIV /)(MULT *)(EXPO ^): "))

        if(op =="+" or op =="-" or op =="/" or op =="*" or op =="^"):
            success3 = True
        else: print("INVALID INPUT, TRY AGAIN")

    #if -else ladder
    if(op=="+"):
        print(f"\n{num1} + {num2} = {num1+num2}")
    elif(op=="-"):
        print(f"\n{num1} - {num2} = {num1-num2}")
    elif(op=="/"):
        print(f"\n{num1} / {num2} = {num1/num2}")
    elif(op=="*"):
        print(f"\n{num1} * {num2} = {num1*num2}")
    elif(op=="^"):
        print(f"\n{num1} ^ {num2} = {num1**num2}")
    else: 
        print("\nINVALID INPUTS TRY AGAIN")
        ask = False

    success4 = False
    while(not success4):
        if(ask):
            temp = str(input("\nkeep going? (YES/NO): ")).upper()
            if(temp=="NO"): 
                power = False 
                success4  =True
            elif(temp=="YES"):
                success4 = True
            else:print("\nINVALID INPUT, TRY AGAIN")
                
'''
power = True
History = []
print("---CALCULATOR---")
while(power):
    request = str(input(" ENTER A PROBLEM: "))
    temp = [request]
    History.extend(temp)    

    
    for i in range(0,request):
        if (48 <= request[i] <=57):
            pass
        elif()

    repower = str(input("Type \"OFF\" or \"ON\" to (dis)continue:")).upper()
    if(repower == "OFF"): power = False

    #the above calculator was something that takes input and identifies all the operators
    #quiet basically like a modern calcii
'''