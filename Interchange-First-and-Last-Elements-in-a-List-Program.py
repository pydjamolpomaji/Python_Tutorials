# Interchange First and Last Element in the List

def SwapList(NewList):
    Size = len(NewList)

    Temp = NewList[0]
    NewList[0] = NewList[Size - 1]
    NewList[Size - 1] = Temp
    return NewList


NewList = [1, 4, 2, 6, 5, 3, 8, 1, 9, 7]
print('Initial List is :', NewList)
print('After Swapping List is :', SwapList(NewList))

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
