# Program 1 :-
# Simple Sort the List
a = [8, 2, 5, 7, 6, 9, 4, 3, 1, 10]
print('Pre List is :', a)
for i in range(len(a)):
    min_value = min(a[i:])
    min_index = a.index(min_value)
    a[i], a[min_index] = a[min_index], a[i]
print('Sorted List is :', a)

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Program 2 :-
# Selection sort Stack Program
a = []
limit = int(input('Please Enter the Limit of Stack :'))


def push():
    print('Initial Stack is :', a)
    if len(a) == limit:
        print('Stack is Full....!!!')
    else:
        element = int(input('Enter the Number :'))
        a.append(element)
        print('Stack is :', a)


def pop():
    if not a:
        print('Stack is Empty...!!')
    else:
        p = a.pop()
        print('Removed Element :', p)
        print('Stack is :', a)


while True:
    print('Please Enter the Correct Operation 1.push 2.pop 3.quit ')
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print('Entered the Incorrect Operations....!!! ')
print('Final Stack is :', a)
for i in range(len(a)):
    min_value = min(a[i:])
    min_index = a.index(min_value)
    a[i], a[min_index] = a[min_index], a[i]
print('Sorted Stack is :', a)
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
