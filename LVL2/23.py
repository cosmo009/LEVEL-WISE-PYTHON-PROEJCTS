"""
* THIS IS A VOWEL COUNTER
* @author gaurang mane
* @date 29.04.2026
"""

def vowel_counter(string):
    #SAMEPLE string = "  HELLO ,!  WORLD _____. ! " - returns 2
    count = 0

    for i in range(len(string)):

        letter = string[i].upper()
        if (letter=="A" or letter=="E" or letter=="I" or letter=="O" or letter=="U"): count+=1   
    return count




power = True
while power:
    print("\n---VOWEL COUNTER---")

    str1 = input("Give me a string and i'll count the vowels: ")
    count = vowel_counter(str1)
    print(f"Vowel count = {count}")

    while True:
        try:
            ask = input("\nRUN AGAIN? (Y/N): ").upper()
            if (ask == "Y" or ask == "N") : break
            else: print("ENTER Y = YES OR N = NO")
        except ValueError:
            print("INVALID INPUT TRY AGAIN")

    if(ask == "Y"): power = True
    elif (ask == "N"): power = False