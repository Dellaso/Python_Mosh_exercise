cmd = ""
has_started = False
while True:
    cmd = input("< ").upper()
    if cmd == "HELP":
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif cmd == "START":
        if has_started:
            print("The car has started.")
        else:
            print("Car started...Ready to go!")
            has_started = True
    elif cmd == "STOP":
        if not has_started:
            print("The car has stopped.")
        else:
            print("Car stop.")
            has_started = False
    elif cmd == "QUIT":
        break
    else:
        print("I don't understand that...")
