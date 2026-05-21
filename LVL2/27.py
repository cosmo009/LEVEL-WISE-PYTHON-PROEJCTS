
"""
* THIS IS AN ARRAY/LIST SORTER - BUBBLE SORT
* @author gaurang mane
* @date 21.05.2026
"""

def sortList(list1):
    sorted_list = list(list1)
    for i in range(0, len(sorted_list)):
        for j in range(0, len(sorted_list) - i - 1):

            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]   # python swapping

    return sorted_list

power = True
while power:
    print("\n---BUBBLE SORTER---")

    list_input = list(map(int, input("ENTER A LIST OF NUMBERS: ").split()))
    list_output = sortList(list_input)
    print(list_output)
    
    


    while True:
        ask = input("\nRUN AGAIN? (Y/N): ").upper()
        if (ask == "Y" or ask == "N"):
            break
        else:
            print("ENTER Y = YES OR N = NO")

    if(ask == "Y"): power = True
    if ask == "Y": power = True
    elif ask == "N": power = False