"""
* THIS IS WORD COUNTER USING FUNCTIONS
* @author gaurang mane
* @date 29.04.2026
"""

def word_counter(string):
    #SAMEPLE string = "  HELLO ,!  WORLD _____. ! " - returns 2
    count = 0

    cond1 = False   #it was letter
    cond2 = False   #it is space
    for i in range(len(string)):

        if (65<=ord(string[i])<=90 or 97<=ord(string[i])<=122):
            cond1 = True   
        elif(string[i] == " "): 
            if(cond1):
                cond2 = True

        if(i==(len(string)-1) and cond1):
            cond2 = True

        if(cond1 and cond2):
                    count+=1
                    cond1 = False
                    cond2 = False
    return count




power = True
while power:
    print("\n---WORD COUNTER---")

    str1 = input("Give me a string and i'll count the words: ")
    count = word_counter(str1)
    print("Word count = "+count)

    while True:
        try:
            ask = input("\nRUN AGAIN? (Y/N): ").upper()
            if (ask == "Y" or ask == "N") : break
            else: print("ENTER Y = YES OR N = NO")
        except ValueError:
            print("INVALID INPUT TRY AGAIN")

    if(ask == "Y"): power = True
    elif (ask == "N"): power = False