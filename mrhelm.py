import time
import os #Was supposed to be for os.system
choice1 = 0 #Redifings variables for bug protecion
choice2 = 0
choice3 = 0
choice4 = 0
have_sword = False
defeated_mon = False

while True:
    print('\x1b[H\x1b[2J', end='') #Actual clearing code.
    time.sleep(1) #Waits for the argument amount of seconds
    print("Someone has kidnapped the entire junior APUSH class, you the teacher Mr. Helm have to find them and save them.") #Prompt
    choice1 = input("Left or Right (1,2): ") #input

    while True:
        time.sleep(0.5)
        print('\x1b[H\x1b[2J', end='')
        if choice1 == '1': #Used to go through "rooms"
            if have_sword == False: #Checks if variable is false
                print("You found the sword.")
                choice2 = input("Pick it up, Go Forward, Go Back. (1,2,3): ")
            else:
                print("There's nothing here.")
                choice2 = 0
                choice4 = input("Go Forward, Go Back. (1,2): ")
            if choice2 == '3' or choice4 == '2':
                break
            while True:
                time.sleep(0.5)
                print('\x1b[H\x1b[2J', end='')
                if choice2 == '1':
                    print('You got the sword.')
                    have_sword = True
                    time.sleep(2)
                    break
                elif choice2 == '2' or choice4 == '1':
                    print('You encountered a split path.')
                    choice5 = input("Left, Right, Go Back (1,2,3): ")
                    if choice5 == '3':
                        break
                    while True:
                        time.sleep(0.5)
                        print('\x1b[H\x1b[2J', end='')
                        if choice5 == '1':
                            print('You encountered ganondorf.')
                        elif choice5 == '2':
                            print('You encountered the riddler.')

                    
            

        if choice1 == '2':
            if defeated_mon == False:
                print("You encountered a powerful monester.")
                choice6 = input("Go Back, Try to Fight (1,2): ")
                if choice6 == '1':
                    while True:
                        time.sleep(0.5)
                        print('\x1b[H\x1b[2J', end='')
                        if have_sword == True:
                            print("You defeated the monster.")
                            defeated_mon = True
                            break
                        else:
                            print('You died. Cause of death = "Monster"')
                            while True:
                                pass
            if choice6 == '1':
                break
        else:
            print("There is nothing here.")
            choice6 = input("Go Back, Go Forward (1,2): ")
            if choice6 == '1':
                    break
            if choice6 == '2':
                while True:
                    time.sleep(0.5)
                    print('\x1b[H\x1b[2J', end='')
                    print('You encountered a split path.')
                    choice7 = input("Left, Right, Go Back (1,2,3): ")
                    if choice7 == '3':
                        break
                    while True:
                        time.sleep(0.5)
                        print('\x1b[H\x1b[2J', end='')
                        if choice7 == '1':
                            print('You encountered the draagon.')
                        elif choice7 == '2':
                            print('There is a quiz answer key, it says 1: Wart, 2: Peanuts, 3: Morty.')
                            choice8 = input("Go Back(1): ")
                            if choice8 == '1':
                                break
                            
