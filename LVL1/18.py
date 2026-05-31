"""
* THIS PROGRAM DISPLAYS THE USE OF A SIMPLE TEXT MENU SYSTEM
* @author gaurang mane
* @date 31.05.2026
"""


power = True
while power:
    print("\n---MENU---")
    print("1. Pizza")
    print("2. Burger")
    print("3. Diet Coke")

    order = int(input("Enter a choice: "))

    match (order):
        case 1:
            n = input("Quantity: ")
            print(f"You've ordered {n} pizzas")
            break
        case 2:
            n = input("Quantity: ")
            print(f"You've ordered {n} burgers")
            break
        case 3:
            n = input("Quantity: ")
            print(f"You've ordered {n} diet cokes")     
            break
        case _:
            print("Invalid choice.")


    while True:
        ask = input("\nRUN AGAIN? (Y/N): ").upper()
        if (ask == "Y" or ask == "N"):
            break
        else:
            print("ENTER Y = YES OR N = NO")

    if ask == "Y":power = True  
    elif ask == "N":power = False           
                                                         