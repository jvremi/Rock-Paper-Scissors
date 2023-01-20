import random

playerPoints = 0
opponentPoints = 0
index = 0

choices = {
    1: ["r", "Rock"],
    2: ["p", "Paper"],
    3: ["s", "Scissors"]
}
choiceAlias = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

def rpsComp(playerChoice, opponentChoice):
    if playerChoice == 'r' and opponentChoice == 'p':
        print("You lose!")
        return 0
    elif playerChoice == 'r' and opponentChoice == 's':
        print("You win!")
        return 1
    elif playerChoice == 'p' and opponentChoice == 'r':
        print("You win!")
        return 1
    elif playerChoice == 'p' and opponentChoice == 's':
        print("You lose!")
        return 0
    elif playerChoice == 's' and opponentChoice == 'p':
        print("You win!")
        return 1
    elif playerChoice == 's' and opponentChoice == 'r':
        print("You lose!")
        return 0

def displayPoints(playerPoints, opponentPoints):   
    print("Current Score:")
    print("Player:", playerPoints)
    print("Oppponent:", opponentPoints)

def checkDig(playerChoice):
    for i in playerChoice:
        while i.isdigit():
            playerChoice = str(input("Error: no numbers allowed \n(R)ock, (P)aper, or (S)cissors? "))
            for i in playerChoice:
                if not i.isdigit:
                    break
    return playerChoice

def checkLength(playerChoice):
    while not len(playerChoice) == 1:
        playerChoice = str(input("Error: please use single characters to make your selection \n(R)ock, (P)aper, or (S)cissors? "))
    return playerChoice

while True:
    print("-------------Game {0}:------------".format(index + 1))
    index = index + 1
    
    playerChoice = str(input("(R)ock, (P)aper, or (S)cissors? "))
    playerChoice = checkDig(playerChoice)
    playerChoice = checkLength(playerChoice)
                    
    #playerNum = int(choices.get())
    #while not playerChoice == 'r' or 'p' or 's':
         #playerChoice = input("(R)ock, (P)aper, or (S)cissors? ")
    print("----------------------------------")
    
    
    randNum = random.randrange(1, 4)
    opponentChoice = choices.get(randNum)
    oChoiceName = choiceAlias[randNum]
    #pChoiceName = choices[]
    
    print("Your Choice:", playerChoice)
    print("Your Opponents choice:", oChoiceName)
    print("----------------------------------")
    
    while playerChoice == opponentChoice:
        playerChoice = input("It's a draw! Guess again ")
        print("----------------------------------")
        
        randNum = random.randrange(1, 4)
        opponentChoice = choices.get(randNum)
        oChoiceName = choiceAlias[randNum]
        
        print("Your Choice:{0}".format(playerChoice))
        print("Your Opponents choice:", oChoiceName)
        print("----------------------------------")
    
    #I am trying to ask opponentChoice to acces the first value from the "Choices" dictionary, but I'm getting an error:
    #"Object of type "None" is not subscriptable"
    #I am guessing this is because opponentChoice is dependent on a random value, how can I resolve this error?
    #opponentChoice is accessed at line #72
    print("rpsComp inputs, \nplayer:", playerChoice[0], "\nopponent:", opponentChoice[0])
    points = rpsComp(playerChoice[0], opponentChoice[0])
    
    if points == 1:
        playerPoints = playerPoints + 1
        print("+1 points to you!")
    elif points == 0:
        opponentPoints = opponentPoints + 1
        print("+1 points to your opponent!")
    print("----------------------------------")
    
    displayPoints(playerPoints, opponentPoints)
    
    if opponentPoints >= 3 or playerPoints >= 3:
        break

print("----------------------------------")
if playerPoints > opponentPoints:
    print("You win!!! Horray!! :D")
elif playerPoints < opponentPoints:
    print("You lost :(")