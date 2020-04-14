#Modules
from os import system
from random import randint


def printWord(letters):
    for i in letters:
        print(i)


def checkWord(word_letters,gues_letters,gues,chance):
    list1 = gues_letters

    for indx, letter in enumerate(word_letters):
        if letter == gues:
            gues_letters[indx] = gues
    
    if list1 == gues_letters:
        chance -= 1

    return gues_letters, chance


def selectWord():
    x = randint(1,5)
    if x == 1:
        return "masa"
    elif x == 2:
        return "kağıt"
    elif x == 3:
        return "demir"
    elif x == 4:
        return "kulaklık"
    elif x == 5:
        return "bilgisayar"


def gameOver(chance):
    if chance == 0:
        return False
    else:
        return True

def main():
    word = selectWord()
    chance = len(word)
    print(chance)

    word_letters = list(word)
    gues_letters = ["~"]*len(word)

    while gameOver(chance):
        system("clear")
        printWord(gues_letters)
        print(chance)
        gues = input("Enter your gues: ")

        gues_letters, chance = checkWord(word_letters,gues_letters,gues,chance)


if __name__ == "__main__":
    main()
