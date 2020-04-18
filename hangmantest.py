#Modules
from os import system
from random import randint

#Prints the word on the screen
def printWord(letters):
    for i in letters:
        print(i+ " ",end="")
 
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
    words = ["headphone","table","computer","paper","network","linux"]
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
def multiPlayer(player1,player2,tour,point1,point2):

    system("clear")
    if tour % 2 == 0:
        print(f"{player1} will select the word and {player2} will know the word!")
        while True:
            try_word = input(f"{player1} enter a word: ")
            system("clear")
            try:
                try_word = int(try_word)
                input("Word must be string! Press Enter.")
            except ValueError:
                word = try_word.lower()
                break
        the_player = player2
        the_point = point2
    else:
        print(f"{player2} will select the word and {player1} will know the word!")
        while True:
            try_word = input(f"{player2} enter a word: ")
            system("clear")
            try:
                try_word = int(try_word)
                input("Word must be string! Press Enter.")
            except ValueError:
                word = try_word.lower()
                break
        the_player = player1
        the_point = point1
    
    chance = len(word)
    word_letters = list(word)
    gues_letters = ["~"]*len(word)
    the_letters = []

    while gameOver(gues_letters,chance):
        system("clear")
        print(f"Guessing: {the_player}    Your Chance: {chance}    The letters you entered: {the_letters}   {the_player} score: {the_point} ")
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
        input(f"Game Over! The Word: {word}. Press Enter.")
        point = 0
        return point
    else:
        point = chance*10
        input(f"You Win! The Word: {word}. You win {point} score! Press Enter.")
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
            system("clear")
            player1 = input("Enter a name for player1: ")
            player2 = input("Enter a name for player2: ")
            while True:
                try:
                    tour = int(input("How many labs (1~): "))
                    if tour < 1:
                        input("Labs must be bigger 0! Press Enter.")
                    else:
                        tour = 2*tour
                        break
                except ValueError:
                    input("Labs must be integer! Press Enter.")
            checker = 0
            point1 = 0
            point2 = 0
            while checker != tour:
                if checker % 2 == 0:
                    point2 += multiPlayer(player1,player2,checker,point1,point2)
                else:
                    point1 += multiPlayer(player1,player2,checker,point1,point2)

                checker += 1
            if point1 > point2:
                input(f"WINNER IS {player1}! {player1} score: {point1}    {player2} score: {point2}. Press Enter.")
            elif point2 > point1:
                input(f"WINNER IS {player2}! {player2} score: {point2}    {player1} score: {point1}. Press Enter.")
            else:
                input(f"DRAW! {player1} score: {point1}    {player2} score: {point2}. Press Enter.")

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
