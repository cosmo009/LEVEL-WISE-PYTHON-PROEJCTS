"""
* THIS IS A BASIC ENCRYPTOR USING CAESOR CIPHER (CHIFT CIPHER)
* @author gaurang mane
* @date 19.05.2026
"""
class WrongTypeException :
    "You have entered an invalid data type as input"
    pass

def shift_cipher(string,shift):
    #SAMEPLE string = "  HELLO ,!  WORLD _____. ! " - returns 2
    ciphered = ""
        
    for i in range(0,len(string)):
        if (65<=ord(string[i])<=90 or 97<=ord(string[i])<=122):    
            if (shift<1 or shift>=26):
                new_shift = int(shift)%26 
                ciphered += chr(int(ord(string[i])) + new_shift)
            else:
                ciphered += chr(int(ord(string[i])) + shift)
        
        else:   ciphered+= str(string[i])
    
    return ciphered



power = True
while power:
    print("\n---VOWEL COUNTER---")

    str1 = input("Give me a string and i'll cipher it: ")
    shift = int(input("Enter an integer to shift it by: "))
    msg = shift_cipher(str1, shift)
    print(f"Encrypted Msg = {msg}")

    while True:
        try:
            ask = input("\nRUN AGAIN? (Y/N): ").upper()
            if (ask == "Y" or ask == "N") : break
            else: print("ENTER Y = YES OR N = NO")
        except ValueError:
            print("INVALID INPUT TRY AGAIN")

    if(ask == "Y"): power = True
    elif (ask == "N"): power = False