import numpy as np

#FUNCTIONS
def matches(dice):
    sums = np.array([(dice == 1).sum(), (dice == 2).sum(), (dice == 3).sum(), (dice == 4).sum(), (dice == 5).sum(), (dice == 6).sum()])
    unq,count = np.unique(dice, axis=0, return_counts=True)

    print("Possible Plays")
    print("---------------")

    for i in sums:
        if i == 2 and unq[count ==2].size == 1:
            print(f"Doubles of: {unq[count == 2]}".replace('[', '').replace(']', ''))
            print(" ")
        elif i == 3:
            print(f"3 of a Kind -  {unq[count == 3]}".replace('[', '').replace(']', ''))
            print(" ")
        elif i == 4:
            print(f"4 of a Kind - {unq[count == 4]}".replace('[', '').replace(']', ''))
            print(" ")
        elif i == 5:
            print("YAHTZEE")
            print(" ")

    for x in unq[count == 2]:
        if unq[count == 2].size == 2:
            print(f"Doubles of: {x}")
            print(" ")

    if unq[count ==2].size == 1 and unq[count == 3].size == 1:
        print("Full House")
        print(" ")
        
    if dice.__contains__(1) and dice.__contains__(2) and dice.__contains__(3) and dice.__contains__(4) and dice.__contains__(5) or dice.__contains__(2) and dice.__contains__(3) and dice.__contains__(4) and dice.__contains__(5) and dice.__contains__(6):
            print("Straight")
            print(" ")
    elif dice.__contains__(2) and dice.__contains__(3) and dice.__contains__(4) and dice.__contains__(5) or dice.__contains__(1) and dice.__contains__(2) and dice.__contains__(3) and dice.__contains__(4):
            print("Small Straight")
            print(" ")


def diceArt(dice):
    if dice == 1:
        return ["-----", "|   |", "| o |", "|   |", "-----",]
    elif dice == 2:
        return ["-----", "|o  |", "|   |", "|  o|", "-----",]
    elif dice == 3:
        return ["-----", "|o  |", "| o |", "|  o|", "-----",]
    elif dice == 4:
        return ["-----", "|o o|", "|   |", "|o o|", "-----",]
    elif dice == 5:
        return ["-----", "|o o|", "| o |", "|o o|", "-----",]
    elif dice == 6:
        return ["-----", "|o o|", "|o o|", "|o o|", "-----",]
    

def resultDisplay(dice):
    for x in range(5):
        for y in dice:
            print(diceArt(y)[x], end='   ')
        print()

    diceStr = np.array2string(dice)
    x = np.char.join('   ', diceStr.replace('[', ' ').replace(']', ''))
    print(x)

    print("\n")

#MAIN
def main():
    diceRoll = np.random.randint(1, 7, size=(5))
    rolls = 1

    print(" ")
    print("1st Roll:")
    print("\n")

    resultDisplay(diceRoll)
    matches(diceRoll)

    while rolls < 3:
        try:
            while True:
                x = int(input("Enter dice to roll (1-5) - Press 'n' to roll:"))

                diceRoll[x-1] = np.random.randint(1, 7)
                    
        except:
            if rolls == 1:
                print(" ")
                print("2nd Roll:")
            elif rolls ==2:
                print(" ")
                print("3rd Roll:")

            print("\n")

            resultDisplay(diceRoll)
            rolls += 1

            print(" ")

            matches(diceRoll)

main()
