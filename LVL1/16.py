"""
* THIS PROGRAM COUNTS THE NUMBER OF DIGITS IN A PROGRAM
* @author gaurang mane
* @date 27.05.2026
"""
def count_digits(n):
    n_ = str(n)
    count=0
    for i in range(0,len(n_)):
         if 48<=ord(str(n_[i]))<=57:  count+=1
        
    return count

power = True
while power:
    print("\n---DIGIT COUNTER---")

    n = input("Enter a number: ")

    ans = count_digits(n)
    print(f"Number of Digits : {ans}")

    while True:
        ask = input("\nRUN AGAIN? (Y/N): ").upper()
        if (ask == "Y" or ask == "N"):
            break
        else:
            print("ENTER Y = YES OR N = NO")

    if ask == "Y":power = True  
    elif ask == "N":power = False           
                                                         