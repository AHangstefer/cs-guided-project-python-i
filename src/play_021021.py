"""
.dir()
.dir("")
.help()
functions to find available methods

"""
Create a function that returns True if the given string has any of the following:

Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters or contains characters that don't fit into any category, return False.

Examples:

csAlphanumericRestriction("Bold") ➞ True
csAlphanumericRestriction("123454321") ➞ True
csAlphanumericRestriction("H3LL0") ➞ False
"""

def csAlphanumericRestriction(input_str):
    if (input_str.isalpha()) or (input_str.isnumeric()):
        return('true')
    else:
        return('false')
# print(csAlphanumericRestriction("rrrrr"))
# print(csAlphanumericRestriction("12355"))
# print(csAlphanumericRestriction("and934f"))
    


"""
Write a function that takes a string as input and returns that string in reverse
order, with the opposite casing for each character within the string.

Examples:

csOppositeReverse("Hello World") ➞ "DLROw OLLEh"
csOppositeReverse("ReVeRsE") ➞ "eSrEvEr"
csOppositeReverse("Radar") ➞ "RADAr"
"""

def switchit(arg):
    return (arg[::-1].swapcase())
#print(switchit("hello"))
#print(switchit("I love EATing Fries"))


def csSquareAllDigits(n):
        return pow(n, 2)
print(csSquareAllDigits(89))



