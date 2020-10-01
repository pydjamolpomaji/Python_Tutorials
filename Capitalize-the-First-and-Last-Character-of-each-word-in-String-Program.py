# Python Program to Capitalize First and Last Character of each Word of a String.
# Using lambda Function.

def capitalize(str):
    return ' '.join(map(lambda s: s[:-1] + s[-1].upper(), s.title().split()))


s = input('Enter the String :')
print("String before Capitalize :", s)
print("String after Capitalize :", capitalize(str))
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
