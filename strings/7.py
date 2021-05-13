"""
We’ll assume that a String s1 and s2 is balanced if all the chars in the s1 are there in s2. characters’ position doesn’t matter.
"""

# s1 = "Ynf"
# s2 = "PYnative"


s1 = "Yn"
s2 = "PYnative"

for chars in s1:
    if chars in s2:
        print("True")

    else:
        print("False")