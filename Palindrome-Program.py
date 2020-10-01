s = input('Enter the String :')


def string(s):
    return s[::-1]


def isPalimdrom(s):
    reverse = string(s)
    if reverse == s:
        return True
    else:
        return False


answer = isPalimdrom(s)
if answer == 1:
    print('{} is Palimdrom'.format(s))
else:
    print('{} is not a Palimdrom'.format(s))
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
