import random

Play_Game = 'yes'

while True:
    if Play_Game == 'yes':
        Answer = random.randint(1, 100)
        Name = input('Enter your Name :')
        print('Welcome ', Name, 'to this Random Guess Game Program.....!!')
        Try_Number = int(input('Please Guess a Number between 1 to 100 :'))
        count = 1
        while Try_Number != Answer:
            if Try_Number > Answer:
                print(Name, ' Your Number is Too Large, Please Enter Smaller than ', Try_Number)
            if Try_Number < Answer:
                print(Name, 'Your Number is Too Small, Please Enter Greater than ', Try_Number)
            Try_Number = int(input('Guess a Number between 1 to 100 :'))
            count += 1
        print('You Got it...!!! Your Number is [' + str(Try_Number) + '] and You tried ' + str(count) + ' Times.')
        if count <= 7:
            print('Congrats', Name, ',You Win the Game...!!')
        else:
            print(Name, "You lose the Game, Let's Play One More Time")
        Play_Game = input('continue ? (Yes / No) :').lower()
    elif Play_Game == 'no':
        print('Thank You So Much', Name, ' For Playing My Game...!!')
        break
    else:
        print("Sorry, I didn't Understand...!!")
        break
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
