started = False

while True:
    command = input('Enter the String : ').lower()
    if command == 'start':
        if started:
            print('Car is already Started...!!')
        else:
            started = True
            print('Now, Car is Started...!!')
    elif command == 'stop':
        if not started:
            print('Car is already Stopped...!! (Please the Start the Car)')
        else:
            started = False
            print('Now, Car is Stopped...!!')
    elif command == 'help':
        print("""
start : to start the car
stop : to stop the car 
quit : to quit the program
""")
    elif command == 'quit':
        print('Thanks for Playing the Car Game...!!')
        break
    else:
        print("Sorry, I didn't understand...!!( Incorrect Input )")
        break
# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
