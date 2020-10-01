Q1 = """1. What is the output of the following Code
var= "James Bond"
print(var[2::-1])
A. Jam
B. dno
C. maJ
D. mes Bon"""

Q2 = """2. Can we use the “else” clause for loops?
for example :-
for i in range(1, 5):
    print(i)
else:
    print("this is else block statement" )
A. Yes
B. No
C. None
D. SyntaxError: invalid syntax"""

Q3 = """3. What is the output of the following code?
var1 = 10
var2 = 20
var = 'py'
print(var1 + var2 + var3)
A. 30
B. 30py
C. 1020py
D. TypeError: unsupported operand type(s) for +: 'int' and 'str'"""

Q4 = """4. Which of the following is not a keyword ?
A. is
B. lambda
C. except
D. open"""

Q5 = """5. How can we generate random numbers in python using methods?
A. random.uniform ()
B. randint()
C. random.random()
D. All of the above"""

Q6 = """6. What is the output of the following Code
Course = 'Python'
def PrintCourse():
  Course = 'Django'
  print("Course Name is :", Course)
PrintCourse()
print("Course Name is :", Course)
A. Course Name is : Django
   Course Name is : Python
B. Course Name is : Python
   Course Name is : Django
C. TypeError 
D. The program failed with errors"""

Q7 = """7. What is the output of the following list assignment
List = [1,4,3,7,5,9,6,2]
List[3:6] = [8,7,0]
print(List)
A. [1, 4, 3, 7, 5, 9, 6, 2]
B. [1, 4, 3, 8, 7, 0, 6, 2]
C. [2, 6, 9, 5, 7, 3, 4, 1]
D. [3, 4, 1, 8, 7, 0, 4, 1]"""

Q8 = """8. What is the output of the following Code
Dictionary = dict([('First',1),('Second',2),('Third',3)])
print(Dictionary)
A. [ (‘First’, 1), (‘Second’, 2), (‘Third’, 3) ]
B. {['First': 1], ['Second': 2], ['Third': 3]}
C. {'First': 1, 'Second': 2, 'Third': 3}
D. SyntaxError: invalid syntax
"""

Q9 = """9. What is the output of the following code
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print(a,b)
A. 10 10
B. 10 20
C. 20 20
D. 20 10"""

Q10 = """10. What is the output of the following code?
list = ['a','b']
list += 'python'
A. ['a', 'b', 'p', 'y', 't', 'h', 'o', 'n']
B. ['a', 'b']
C. ['a', 'b','python']
D. TypeError: can only concatenate list
"""
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

QuestionAnswerDict = {Q1: 'C', Q2: 'A', Q3: 'D', Q4: 'D', Q5: 'D', Q6: 'A', Q7: 'B', Q8: 'C', Q9: 'D', Q10: 'A'}

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import datetime

Name = input('Enter Your Name :').capitalize()


def TimeInfo():
    date_now = datetime.datetime.now()
    th = int(date_now.strftime('%H'))
    if th < 12:
        wish = "Good Morning"
    elif th < 16:
        wish = "Good Afternoon"
    elif th < 19:
        wish = 'Good Evening'
    else:
        wish = "Good Night"
    print('Hello,', wish, Name)


TimeInfo()
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
print(Name, 'Welcome to Python QuizWorld...!!')
Score = 0
print(Name, 'Your Initial Score is :', Score)

for i in QuestionAnswerDict:
    print('=-' * 75)
    print(i)
    Skip = input('Do you want to Skip the Question (yes/no) :')
    if Skip == 'yes':
        continue
    Answer = input('Please Enter Your Answer :').upper()
    if Answer == QuestionAnswerDict[i]:
        print('Correct Answer,', Name, 'You Got 1 Point')
        Score += 1
        print('Your Current Score is :', Score)
    else:
        print('Wrong Answer,', Name, 'You Loss 1 Point')
        Score -= 1
        print('Your Current Score is :', Score)
        print('=-' * 10, 'Correct Answer is Option :', QuestionAnswerDict[i], '=-' * 10)
    Quit = input('Do you want to Quit the Quiz (yes/no) :')
    if Quit == 'yes':
        Sure = input('Are you Sure,(yes/no) :')
        if Sure == 'yes':
            break
print('=-' * 75)
print('Final Score is :', Score)

if Score >= 1:
    print('You win the Quiz World...You got Positive Marks..!!')
elif Score == 0:
    print('You got Zero Marks')
else:
    print('You loos the Quiz World...You got Negative Marks..!!')
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
