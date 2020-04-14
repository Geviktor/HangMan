from os import system
from random import randint

while True:
    system("clear")
    print("""
                Adam Asmaca Oyununa Hoşgeldin!
                    [1] Bilgisayara Karşı
                    [2] İki kişilik
                    [Q] Çıkış
    
    """)
    choice = input("Tercihin : ")
    choice = choice.lower()

    if choice == "1":
        ran = randint(1,5)
        if ran == 1:
            secret_word = "kalem"
            live = 7
        elif ran == 2:
            secret_word = "paragraf"
            live = 9
        elif ran == 3:
            secret_word = "telefon"
            live = 8
        elif ran == 4:
            secret_word = "sandalye"
            live = 9
        else:
            secret_word = "bilgisayar"
            live = 11
        gues_word = ""
        system("clear")
        char_check = list()
        (args) = char_check
        control = -1
        while live > 0:
            character_left = 0
            print(f"Can:{live}   Girdiğin Harfler: {args}")
            for char in secret_word:
                if char in gues_word:
                    print(char)
                else:
                    print("~")
                    character_left += 1
            if character_left == 0:
                print("BRAVO Kazandın!")
                input("Devam Etmek İçin [ENTER]'e Bas")
                break
            gues = input("Bir harf girin:")
            gues = gues.lower()
            char_check += gues
            system("clear")
            if len(gues) > 1:
                print("Yalnızca Bir Harf Girebilirsin!Canın azaldı!")
                live -= 1
            else:
                gues_word += gues
                if gues not in secret_word:
                    print("Kelimenin İçinde Böyle Bir Harf Yok! Canın Azaldı!")
                    live -= 1
            if live == 0:
                print("Malesef Kaybettin! KELİME: {}".format(secret_word))
                input("Devam Etmek İçin [ENTER]'e Bas")
    if choice == "2":
        system("clear")
        name1 = input("1. Oyuncunun Adı: ")
        name2 = input("2. Oyuncunun Adı: ")
        system("clear")
        name1_score = 0
        name2_score = 0
        tour = 1
        while True:
            if tour == 1:
                print(f"Gizli Kelimeyi {name1} Girecek! {name2} ise tahmin etmeye çalışacak!")
                secret_word = input(f"{name1} gizli kelimeyi gir: ")
                secret_word = secret_word.lower()
                gues_word = ""
                live = 8
                system("clear")
            elif tour == 2:
                print(f"Gizli Kelimeyi {name2} Girecek! {name1} ise tahmin etmeye çalışacak!")
                secret_word = input(f"{name2} gizli kelimeyi gir: ")
                secret_word = secret_word.lower()
                gues_word = ""
                live = 8
                system("clear")
            else:
                print(f"{name1} : {name1_score}         {name2} : {name2_score}")
                if name1_score > name2_score:
                    print(f"{name1} Kazandı! Bravo")
                    input("Devam Etmek İçin [ENTER]'e Bas")
                    break
                elif name1_score == name2_score:
                    print("BERABERE KALDINIZ!")
                    input("Devam Etmek İçin [ENTER]'e Bas")
                    break
                else:
                    print(f"{name2} Kazandı! Bravo")
                    input("Devam Etmek İçin [ENTER]'e Bas")
                    break
            while live > 0:
                print(f"        Can : {live}      {name1}:{name1_score}    {name2}:{name2_score} ")
                character_left = 0
                for char in secret_word:
                    if char in gues_word:
                        print(char)
                    else:
                        print("~")
                        character_left += 1
                if character_left == 0:
                    if tour == 1:
                        print(f"Bravo {name2}! Kelimeyi Buldun!")
                        input("Devam Etmek İçin [ENTER]'e Bas")
                        system("clear")
                        name2_score += 50
                        tour += 1
                        break
                    if tour == 2:
                        print(f"Bravo {name1}! Kelimeyi Buldun!")
                        input("Devam Etmek İçin [ENTER]'e Bas")
                        system("clear")
                        name1_score += 50
                        tour += 1
                        break
                gues = input("Bir harf girin:")
                system("clear")
                if len(gues) > 1:
                    print("Yalnızca Bir Harf Girebilirsin!Canın azaldı!")
                    live -= 1
                else:
                    gues_word += gues
                    if gues not in secret_word:
                        if tour == 1:
                            print("Kelimenin İçinde Böyle Bir Harf Yok! Canın Azıldı! 10 Puan kaybettin")
                            name2_score -= 10
                            live -= 1
                        else:
                            print("Kelimenin İçinde Böyle Bir Harf Yok! Canın Azıldı! 10 puan kaybettin")
                            name1_score -= 10
                            live -= 1
                    else:
                        if tour == 1:
                            print("Bu Harf Kelimenin İçinde Var! 20 puan kazandın!")
                            name2_score += 20
                        else:
                            print("Bu Harf Kelimenin İçinde Var! 20 puan kazandın!")
                            name1_score += 20
                if live == 0:
                    if tour == 1:
                        print(f"{name2}Malesef Kaybettin! {secret_word} ")
                        input("Devam Etmek İçin [ENTER]'e Bas")
                        system("clear")
                        tour += 1
                        break
                    elif tour == 2:
                        print(f"{name1}Malesef Kaybettin! {secret_word} ")
                        input("Devam Etmek İçin [ENTER]'e Bas")
                        system("clear")
                        tour += 1
                        break

    if choice == "q":
        quit()


