power = True
while power:

    print("\n---MULTIPLICATION TABLES---\n")

    while True:
        try:
            table = float(input("enter the required multiplication table: "))
            break
        except ValueError:
            print("INVALID INPUT TRY AGAIN")
        
    print("\n")
    for i in range(1,11):
        print(f"{table} x {i} = {table*i}")
    
    while True:
        try:
            ask = input("\nRUN AGAIN? (Y/N): ").upper()
            if (ask == "Y" or ask == "N") : break
            else: print("ENTER Y = YES OR N = NO")
        except ValueError:
            print("INVALID INPUT TRY AGAIN")

    if(ask == "Y"): power = True
    elif (ask == "N"): power = False