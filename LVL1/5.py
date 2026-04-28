"""
* This program is a display of mulitple methods to swap two variables
* @author gaurang mane
* @date 25.04.2026
"""

#lets take some user input to make it fun and interactive
a = input("Enter value for 'a': ")
b = input("Enter value for 'b': ")

#only in python we can swap the variables with method below
a,b = b,a
print(f"\nFirst Swap: a = {a} ; b = {b}")

#otherwise we must use a third variable (here temp)
temp = a
a = b
b = temp
print(f"\nSecond Swap: a = {a} ; b = {b}")