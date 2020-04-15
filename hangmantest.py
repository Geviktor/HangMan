#Modules
from os import system
from random import randint

#Prints the word on the screen
def printWord(letters):
    for i in letters:
        print(i)

#Checks the word. If letter is not in the word return chance - 1. If letter is in the word return letter.
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

#A random function for select the word.
def selectWord():
    words = ["kulaklık","masa","bilgisayar","demir","kağıt","kalem"]
    x = randint(0,5)
    return words[x]

#Game ending function. If chance = 0, the game is over. If you know the word, the game is over.
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

#For play with yourself.
def singlePlayer(total_score):
    system("clear")
    word = selectWord()
    chance = len(word)

    word_letters = list(word)
    gues_letters = ["~"]*len(word)
    the_letters = []

    while gameOver(gues_letters,chance):
        system("clear")
        print(f"Total Score: {total_score}        Your Chance: {chance}     The letters you entered: {the_letters} \n")
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
        input(f"Game Over! Total Score: {total_score} The Word: {word}. Press Enter.")
        return 0
    else:
        point = chance*10
        input(f"You Win! You earned {point} point! The Word: {word}. Press Enter.")
        return point

#For play with a friend.
def multiPlayer(player1,player2,tour):

    system("clear")
    if tour % 2 == 0:
        print(f"{player1} will select the word and {player2} will know the word!")
        while True:
            system("clear")
            try_word = input(f"{player1} enter a word: ")
            try:
                try_word = int(try_word)
                input("Word must be string! Press Enter.")
            except ValueError:
                word = try_word.lower()
                break
        the_player = player2
    else:
        print(f"{player2} will select the word and {player1} will know the word!")
        while True:
            system("clear")
            try_word = input(f"{player2} enter a word: ")
            try:
                try_word = int(try_word)
                input("Word must be string! Press Enter.")
            except ValueError:
                word = try_word.lower()
                break
        the_player = player1
    
    chance = len(word)
    word_letters = list(word)
    gues_letters = ["~"]*len(word)
    the_letters = []

    while gameOver(gues_letters,chance):
        system("clear")
        print(f"Guessing: {the_player}    Your Chance: {chance}    The letters you entered: {the_letters} ")
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
        point = 0
        return point
    else:
        print(f"You Win! The Word: {word}")
        point = chance*10
        return point
 
#The main function
def main():
    while True:
        system("clear")
        print("""
                Welcome to Hangman Game!

                [1] Play With A Friend
                [2] Play with Yourself
                [Q] Quit

        """)
        choice = input("Enter choice: ")
        choice = choice.lower()

        if choice == "1":
            pass
        elif choice == "2":
            total_score = 0
            point = 1
            while point > 0:
                point = singlePlayer(total_score)
                total_score += point

        elif choice == "q":
            print("See you later! :)")
            break
        else:
            input("Invalid value! Just you can type: 1, 2, Q. Press Enter.")


if __name__ == "__main__":
    main()
