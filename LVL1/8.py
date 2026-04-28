"""
* @author gaurang mane
* @date 28.04.2026
"""
'''
#THIS IS A SIMPLE INTEREST CALCULATOR BASICALLY USIGN A FORMULA TO SOLVE SOME SIMPLE 5TH GRADE MATHS
ik it's pretty stupid
'''

while True:
    try:
        principal = float(input("\nPrincipal ($): "))
        if 0<=principal: break
        else: print("principal value cannot be negative...try again")
    except ValueError:
        print("Invalid input value for principal amount.")

while True:
    try:
        time = float(input("\nTime (years): "))
        if 0<=time: break
        else: print("time value cannot be negative...try again")
    except ValueError:
        print("Invalid input value for time. acceptable units are in years")

while True:
    try:
        rate = float(input("\nRate (%): "))
        if 0<=rate<=100: break
        else: print("rate value out of range (0-100)...try again")
    except ValueError:
        print("Invalid input value for rate. acceptable units are in percentage (0-100)")

simple_interest = principal*rate*time /100
total_amt = principal + simple_interest
print(f"\nSIMPLE INTEREST = {simple_interest}$")
print(f"TOTAL AMOUNT = {total_amt}")
