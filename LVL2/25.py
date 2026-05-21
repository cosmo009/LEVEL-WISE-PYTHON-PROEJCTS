
"""
* FINDING MAX AND MIN WITHOUT USING INBUILT FUNCTIONS
* @author gaurang mane
* @date 21.05.2026
"""

def findMin(list1):
    obj_list = list(list1)
    ans = obj_list[0]
    for i in range(0, len(obj_list)):
        if ans > obj_list[i]: ans = obj_list[i]

    return ans

def findMax(list1):
    obj_list = list(list1)
    ans = obj_list[0]
    for i in range(0, len(obj_list)):
        if ans < obj_list[i]: ans = obj_list[i]

    return ans

power = True
while power:
    print("\n---FIND MIN / MAX---")

    list_input = list(map(int, input("ENTER A LIST OF NUMBERS: ").split()))
    min_ans = findMin(list_input)
    max_ans= findMax(list_input)

    print(f"Maximum = {max_ans} \nMinimum = {min_ans} ")
    
    


    while True:
        ask = input("\nRUN AGAIN? (Y/N): ").upper()
        if (ask == "Y" or ask == "N"):
            break
        else:
            print("ENTER Y = YES OR N = NO")

    if(ask == "Y"): power = True
    if ask == "Y": power = True
    elif ask == "N": power = False