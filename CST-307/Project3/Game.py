#The 100 Game
#Tyler Nichols
#CST-215
    #Menu
print('Welcome to the game\n---MENU---\n1 - Multiplayer Game\n2 - Start Computer Game\n3 - Quit Game')
choice = int((input()))
    #Placed two if/elif statements because the code was buggy when I kept them together
if choice == 1:
    print("Good luck have fun")
elif choice == 2:
    print("Sick, humans enjoying robots going head-to-head")
elif choice == 3:
    print("Fine, I didn't want you to play anyways")
    #Placed three exit points to tell where the user exited the program
    exit(0)
    #Player vs. Player game
if choice == 1:
    #Main Game Loop
    #This while loop keeps the game rolling until the break statement which only hits until the totalNumber while loop is satisfied
    while True:
        print("Input Player 1's name, for my sake")
        oneName = input()
        print("Input player 2's name, don't worry I won't tell anyone you are playing alone... loser")
        twoName = input() 
        print("Welcome to The Game," + oneName + " and " + twoName)
        print("You will each have a turn to choose a number between 1 and 10, if you try to pick one higher or lower I will find you and I will destroy you")
        print("The first person to reach 100 is the winner but really guys does winner matter as lon- OF COURSE WINNER MATTERS DESTROY THAT FOOL")
        print("Have fun, don't lose")
        print("Player One, please enter the minimum input(don't go lower than 0)")
        lowerEnd = input()
        print("Player Two, please enter the maximum input")
        higherEnd = input()
        print("Please enter the maximum score")
        scoreSum = input()
        #This starts the game counter at 0
        totalNumber = 0
        #Main while loop that counts the game counter
        while totalNumber <= int(scoreSum):

            numberOne = input(oneName + ', give me a number between 1 and 10.')
            numberOne = int(numberOne)
            #Placed two if/else statements to ensure the two players don't insert a number < or > than 0 or 10
            if numberOne > int(higherEnd) or numberOne < int(lowerEnd):
                numberOne = input(oneName + ', give me a number between 1 and 10.')
            else:
                totalNumber += numberOne
            print("Got it, " + oneName + "! Below is the total right now:")
            print(totalNumber)
            # this if statment is because the user would run through this so quickly that sometimes player one would
            # hit 100 or over 100 but player two would still get his turn this fixes that with an exit statement
            if totalNumber >= int(scoreSum):
                exit(2)
            else:
                numberTwo = input(twoName + ', give me a number between 1 and 10.')
                numberTwo = int(numberTwo)
            #Second if/else statement of player two
            if numberTwo > int(higherEnd) or numberTwo < int (lowerEnd):
                numberTwo = input(oneName + ', give me a number between 1 and 10.')
            else:
                totalNumber += numberTwo
            print("Got it, " + twoName + "! Below is the total right now:")
            print(totalNumber)
            #Break point to exit the Main Game while loop after the totalNumber while loop is satisfied
            print("out of" + scoreSum)
        break
            #Computer vs. Computer if statement
if choice == 2:
    print("Robot one is named Jeff and Robot two is named Jose.... not that you care dirty human")
    print("Watch how fast my friends can play this game")
    print("Input Jeff's name right here")
            #Require user to enter robots name so its like play button but also a fun little side thing for the user to
            # interact with
    RobotOne = input()
    print("Input Jose's name right here")
    RobotTwo = input()
            #total number counter starting at 0
    totalNumber = 0
            #main while loop for the computer game
            #didnt include Main Game Loop because the computer would run through this and not present any errors such as
            # symbols or characters
            #so I didnt run into the risk of the while loop crashing
    while totalNumber <= 100:
            #for some reason my randint function wouldnt work without this library that I pulled from the internet
        from random import randint
        RobotOne = randint(1, 10)
        totalNumber += RobotOne
        print(RobotOne)
            #this if statment is because the computer would run through this so quickly that sometimes player one would
            #hit 100 or over 100 but player two would still get his turn this fixes that with an exit statement
        if totalNumber <= 0:
                exit(2)
        else:
            RobotTwo = randint(1, 10)
            totalNumber += RobotTwo
        print(RobotTwo)
        print("This is the total so far")
        print(totalNumber)
    print(totalNumber)
    print("Told you my friends were fast")
