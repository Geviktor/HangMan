#modules
from os import system
from random import randint


def printWord(letters):
    for i in letters:
        print(i)


def checkWord(word_letters,gues_letters,gues,chance):
    list1 = []
    for i in gues_letters:
        list1.append(i)

    for indx, letter in enumerate(word_letters):
        if letter == gues:
            gues_letters[indx] = gues
    
    if list1 == gues_letters:
        chance -= 1
    return gues_letters, chance


def selectWord():
    words = ["kulaklık","masa","bilgisayar","demir","kağıt","kalem"]
    x = randint(0,5)
    return words[x]

def gameOver(gues_letters,chance):
    checker = 0
    for i in gues_letters:
        if i == "~":
            checker += 1

    if chance == 0:
        return False
    elif checker == 0:
        return False
    else:
        return True

def singlePlayer():
    word = selectWord()
    chance = len(word)
    print(chance)

    word_letters = list(word)
    gues_letters = ["~"]*len(word)
    the_letters = []

    while gameOver(gues_letters,chance):
        system("clear")
        print(f"Your Chance: {chance}     The letters you entered: {the_letters} \n")
        printWord(gues_letters)
        gues = input("\nEnter your gues: ")

        try:
            gues = int(gues)
            input("Letter must be string! Press Enter.")
        except ValueError:
            if len(gues) > 1:
                input("Letter must be 1 character! Press Enter.")
            else:
                gues = gues.lower()
                if gues in the_letters:
                    input("You used this letter! Press enter.")
                else:
                    the_letters.append(gues)
                    gues_letters, chance = checkWord(word_letters,gues_letters,gues,chance)

    if chance == 0:
        print(f"Game Over! The Word: {word}")
    else:
        print(f"You Win! The Word: {word}")
        

def main():
    singlePlayer()


if __name__ == "__main__":
    main()
