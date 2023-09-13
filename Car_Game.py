command = ""
started = False
while True:
    command = input("🚗: What I need to do? ").lower()
    if command == "start":
        if started:
            print("\nCar is already started! Try other command\n")
        else:
            started = True
            print("\nCar started...\n")

    elif command == "stop":
        if not started:
            print("\nCar is already stopped! Try other command\n")
        else:
            started = False
            print("\nCar stopped.\n")

    elif command == "help":
        print("""
*start - to start the car 
              
*stop - to stop the car 
              
*quit - to exit
        """)

    elif command == "quit":
        print("\nThe game has stopped\n")
        break

    else:
        print("\nType 'help' for available commands\n")



