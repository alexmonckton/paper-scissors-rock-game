import random
import getpass
choices = ["Rock","Paper","Scissors"]
def getname(player):
    name = input("Please enter your name player %s: " % player)
    while len(name) < 2:
        name = input("Please enter a name that is at least 2 characters, player %s: " % player)
    print("\n")
    return name

def game(nameA, nameB, rounds, scoreA, scoreB):
    if random.randrange(0, 2) == 0:
        nameA, nameB = nameB, nameA
        scoreA, scoreB = scoreB, scoreA
    print(nameA + " has been randomly selected to start the game.")
    choiceA = MakeChoice(nameA)
    choiceB = MakeChoice(nameB)
    print("\nResults: %s (%s) vs %s (%s)" %(nameA, choices[choiceA-1], nameB, choices[choiceB-1]))
    if choiceA == choiceB + 1 or choiceA == choiceB - 2:
        print("Congratulations %s, you've won the match!" % nameA)
        scoreA += 1
    elif choiceB == choiceA + 1 or choiceB == choiceA - 2:
        print("Congratulations %s, you've won the match!" % nameB)
        scoreB += 1
    else:
        print("It's a tie!")
    if rounds > 1:
        anotherround(nameA, nameB, rounds, scoreA, scoreB)
    else:
        print("\nFINAL OVERALL SCORE:\n%s: %i\n%s: %i" % (nameA, scoreA, nameB, scoreB))
        if scoreA > scoreB:
            print("CONGRATULATIONS %s! YOU ARE THE OVERALL WINNER!" % nameA)
        elif scoreB > scoreA:
            print("CONGRATULATIONS %s! YOU ARE THE OVERALL WINNER!" % nameB)
        else:
            print("YOU BOTH TIED!")
            if (input("One more round for tiebreaker? y/n: ").lower() == "y"):
                game(nameA, nameB, 1, scoreA, scoreB)


def MakeChoice(name):
    print("\n" + name + " please choose your weapon:\n1. Rock\n2. Paper\n3. Scissors")
    while(True):
        try:
            choice = int(getpass.getpass("Enter your choice (without someone seeing): "))
        except ValueError:
            print("Please enter a number from 1 to 3.")
            continue
        if choice < 1 or choice > 3:
            print("Please enter a number from 1 to 3.")
            continue
        break
    return choice

def anotherround(nameA, nameB, rounds, scoreA, scoreB):
    rounds -= 1
    print("\nCURRENT SCORES:\n%s: %i\n%s: %i" % (nameA, scoreA, nameB, scoreB))
    if rounds == 1:
        input("Press enter for the last round!")
    else:
        input("Press enter for another round. %i rounds to go!" % rounds)
    print("\n")
    game(nameA, nameB, rounds, scoreA, scoreB)

print("\nWelcome to Rock, Paper, Scissors.")
nameA = getname("A")
nameB = getname("B")
rounds = int(input("Enter the number of rounds you would like to play: "))
print("\n")
game(nameA, nameB, rounds, 0, 0)
