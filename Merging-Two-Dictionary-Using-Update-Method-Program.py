# Python code to merge dict using update() method
def Merge(dict1, dict2):
    M = dict2.update(dict1)
    return (M)


dict1 = {'a': 2, 'm': 4, 'o': 6, 'l': 8}
dict2 = {'n': 1, 'e': 3, 'r': 5, 'h': 7}

Merge(dict1, dict2)

# Changes made in dict2
print(dict2)
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
