"""
* @reverse function: reverses the entire order of letters
* @param string: string in question
"""
def reverse(string):
        return string[::-1]

"""
* @reverse function: reverses the entire order of words
* @param string: string in question
"""
def reverse_word_order(string):
    rev = []
    temp = ""
    cursor_end = len(string)-1
    for cursor_start in range(len(string)-1,-1,-1):
        #cursor_start will store WORD index
        #cursor_end will store SPACE index
        
        #IF THE join method didnt exist (like in other languages) then we would've to create the method
        '''
        def join(lis1[]):
            temp = ""
            for i in lis1:
                temp+=i
            return temp
        '''

        if(string[cursor_start]==" " or cursor_start==0): 
            rev.append(string[cursor_start:cursor_end+1])
            cursor_end=cursor_start
    return temp.join(rev)



"""
* THIS PROGRAM REVERSES STRINGS USING FUNCTIONS
* @author gaurang mane
* @date 29.04.2026
"""
power = True
while power:
    a = input("Enter a String: ")
    print(f"\nOriginal String : {a}\nReversed String : {reverse(a)}")

    b = input("\nEnter another String: ")
    print(f"\nOriginal String : {b}\nReversed String : {reverse_word_order(b)}")


    while True:
        try:
            ask = input("\nRUN AGAIN? (Y/N): ").upper()
            if (ask == "Y" or ask == "N") : break
            else: print("ENTER Y = YES OR N = NO")
        except ValueError:
            print("INVALID INPUT TRY AGAIN")

    if(ask == "Y"): power = True
    elif (ask == "N"): power = False