# Program 1 :-
# Python Program to check if a Number is Positive, Negative or Zero
num = float(input('Enter the Number :'))
if num > 0:
    print('{} is Positive Number'.format(num))
elif num == 0:
    print('{} is Zero'.format(num))
else:
    print('{} is Negative Number'.format(num))
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Program 2 :-
# Check Number is Even or Odd.
num = int(input('Enter the Number :'))
if num % 2 == 0:
    print('{0} is Even Number'.format(num))
else:
    print('{0} is Odd Number'.format(num))


# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Program 3 :-
# Find the Biggest Number using function.
def Big(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
    return


x = int(input('Enter the First Number :'))
y = int(input('Enter the Second Number :'))
z = int(input('Enter the Third Number :'))

print('Biggest Number is :', Big(x, y, z))

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Program 4 :-
# Find the Biggest Number in List
numbers = [10, 50, 40, 20, 30, 60, 143, 80, 70]
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print('Biggest Number in list is :', max)

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
