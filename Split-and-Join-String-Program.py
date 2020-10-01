# Python program to split a string and Join the String

def Split_String(String):
    List_String = String.split(' ')
    return List_String


def Join_String(List_String):
    String = '-'.join(List_String)
    return String


if __name__ == '__main__':
    String = input('Enter the Sentence : ')
    List_String = Split_String(String)
    print('Split String is :', List_String)
    New_String = Join_String(List_String)
    print('Join String is :', New_String)
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
