# car game
command = ""
started = False
while command != 'quit':
    command = input('what is do you want to do with your car? ')
    if command.lower() == 'start':
        if started:
            print('car is already started')
        else:
            started = True
            print("Car started")
    elif command.lower() == 'stop':
        if not started:
            print('car is not started')
        else:
            started = True
            print('car stopped')
    elif command.lower() == 'help':
        print("""
    start
    stop
    quit""")
        break
    else:
        print("I dont understand")

