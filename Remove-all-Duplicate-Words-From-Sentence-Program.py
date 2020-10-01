# 1. This Program without using any External Library

Sentence = input('Enter the Sentence :')

Split_Sentence = Sentence.split()
k = []
for i in Split_Sentence:
    if (Sentence.count(i) > 1 and (i not in k) or Sentence.count(i) == 1):
        k.append(i)
print(' '.join(k))

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# 2. In this Program we used a Python Counter Module
from collections import Counter


def Remove_Duplicates(input):
    input = input.split(" ")
    for i in range(0, len(input)):
        input[i] = "".join(input[i])
    UniqW = Counter(input)
    print(' '.join(UniqW.keys()))


Sentence = input('Enter the Sentence :')
Remove_Duplicates(Sentence)

# Driver program
# if __name__ == "__main__":
#     input = 'Python is great and Django is also great'
#     Remove_Duplicates(input)
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
