"""
* SIMPLE GRADE CALCULATOR WITH SOME ERROR HANDLING
* @author gaurang mane
* @date 29.04.2026
"""
print("\n---GRADE CALCULATOR---")
while True:
    try:
        marks = float(input("Enter your mark's percentage (%): "))
        if 0<=marks<=100 : break
        else: print("Invalid amount of marks")
    except ValueError:
        print("Invalid input. Try Again.")
    
if 90<=marks<=100 : grade = "A+"
elif 80<=marks : grade = "A-"
elif 70<=marks : grade = "B+"
elif 60<=marks : grade = "B-"
elif 50<=marks : grade = "C+"
elif 40<=marks : grade = "C-"
elif  0<=marks : grade = "F"

print(f"\nGRADE = {grade}")