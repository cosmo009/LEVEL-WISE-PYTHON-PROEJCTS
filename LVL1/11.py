"""
* THIS PROGRAM SHOWS DIFFERENT WAYS TO FIND SUM OF N NUMBERS
* @author gaurang mane
* @date 29.04.2026
"""
power = True
while power:

    print("\n---SUM OF N NUMBERS---\n")

    while True:
        try:
            n = int(input("enter number to find sum of integers upto: "))
            break
        except ValueError:
            print("INVALID INPUT TRY AGAIN")

    sum = 0

    #METHOD 1 - LOOPS
    for i in range(n+1): sum+=i
    
    #METHOD 2 - FORMULA
    sum = n*(n+1)/2

    print(f"\n SUM OF {n} integers = {sum}")

    while True:
        try:
            ask = input("\nRUN AGAIN? (Y/N): ").upper()
            if (ask == "Y" or ask == "N") : break
            else: print("ENTER Y = YES OR N = NO")
        except ValueError:
            print("INVALID INPUT TRY AGAIN")

    if(ask == "Y"): power = True
    elif (ask == "N"): power = False