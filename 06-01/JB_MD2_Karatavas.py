import os
from random import choice

def invoke_hangman(word_to_guess, guess_count):
    os.system('cls')
    case_insensitive = True
    if case_insensitive:
        word_to_guess = word_to_guess.lower()

    masked_word = "*" * len(word_to_guess)
    guess_iteration = 0
    char_guessed = ""

    print(f"Tev ir dotas {guess_count} iespējas, lai atminētu slepeno vārdu '{masked_word}'.")

    while "*" in masked_word and guess_count != 0:
        guess_char = input("Lūdzu, ievadi burtu: ")

        if not guess_char:
            print("Ievadi burtu!")
            continue
        if len(guess_char) > 1:
            print("Ievadi vienu burtu!")
            continue
        if case_insensitive:
            guess_char = guess_char.lower()
        if guess_char in masked_word: # Continue if char has been guessed already.
            print(f"'{guess_char}' jau ir uzminēts. Tas is slepenajā vārdā '{masked_word}'")
            continue
        if guess_char in char_guessed: # Continue if chat has been guessed already.
            print(f"Tu jau meģināji '{guess_char}'! Tas ir mineto burtu virknē '{char_guessed}'")
            continue

        for i, char in enumerate(word_to_guess):
            if char in guess_char:
                masked_word = masked_word[:i] + char + masked_word[i + 1:]

        if guess_char not in word_to_guess:
            if guess_char not in char_guessed:
                guess_count -= 1
                char_guessed = char_guessed + " " + guess_char

        if len(char_guessed) > 0:
            print(f"Slepenais vārds: {masked_word}; Minējumu skaits: {guess_count}; Minētie burti: {char_guessed}")
        else:
            print(f"Slepenais vārds: {masked_word}; Minējumu skaits: {guess_count}; Atminēti {(len(masked_word) - masked_word.count('*'))}")

    if guess_count == 0:
        print(f"Piedodm tu neatminēji vārdu. Pareizais vārds ir {word_to_guess}.")
        input("Spied 'Enter' lai turpinātu...")
        return False
    if "*" not in masked_word:
        print("Malacis, tu atminēji vārdu.")
        input("Spied 'Enter' lai turpinātu...")
        return True

words_list = [
    "Suns", "Mašīna", "Sūniņš", "Zirgs", "Māja", "Rotaļlieta", "Puķe", "Dators", "Rokassprādze", 
    "Ceļš", "Telefons", "Grāmata", "Poga", "Skapis", "Krēsls", "Rotaļlieta", "Kakts", "Durvis", 
    "Putns", "Ābols", "Upe", "Galds", "Zīmulis", "Kokvilna", "Ķekars", "Pūce", "Ritenis", "Galda spēle",
    "Riņķis", "Pilis", "Sarkans", "Zābaks", "Kaste", "Spogulis", "Cepure", "Krēsls", "Dzirnavas",
    "Skurstenis", "Vējš", "Kāja", "Zvaigzne", "Autors", "Fotoaparāts", "Kurpes", "Vilkābele", "Vilkābe",
    "Vilkāta", "Krēsla spilvens", "Aizgājiens", "Peldkostīms", "Kājene", "Lācis", "Aizbāznis", "Telpa",
    "Zāle", "Bumba", "Sniegs", "Pūlis", "Spārni", "Mežs", "Sala", "Okeāns", "Svītrainis", "Zupa",
    "Sēdeklis", "Rokasgrāmata", "Lapas", "Tekstils", "Zābaki", "Soma", "Kvadrāts", "Cilnis", "Ritenis",
    "Pūlis", "Pogas", "Zivs", "Trusis", "Gredzens", "Rokassprādze", "Cepure", "Šalle", "Sieviete",
    "Vīrietis", "Kapuce", "Rokas", "Kājas", "Austiņa", "Spārns", "Vilnis", "Lietus", "Sniegs", "Vējš"
]

failed_guess_count = 10
game_menu_answer = 99
guessed_words = []
win = 0
loss = 0
words_list = list(set(words_list))

while game_menu_answer != 2:
    os.system('cls')
    print("#####################################################", end="\n\n")

    print("Laipni aicināti karātavu spēlē!")
    print(f"Spēlē ir '{len(words_list)}' minamo vārdu.", end="\n\n")
    print(f"Reizes uzvarets: {win}; Rezes zaudets: {loss}")

    print("Izvēies opciju:")
    print("0 - Ielādēt vārdus no faila '.\minamie_vardi.txt'.")
    print("1 - Sākt spēli")
    print("2 - Iziet!", end="\n\n")

    if guessed_words:
        print(f"Uzminetie vardi: {guessed_words}")
    print("#####################################################")

    game_menu_answer = input("Izvelies opciju: ")
    game_menu_answer = int(game_menu_answer)
    if game_menu_answer not in [0, 1, 2]:
        print("Ievadi pareizo opciju - 0, 1, 2")

    if game_menu_answer == 0:
        f = open('minamie_vardi.txt', 'r', encoding='utf-8')
        f_content = f.read()
        f_content = f_content.splitlines()
        print(f"Minamo vārdu daudzums palielinats no '{len(words_list)}' uz {len(words_list + f_content)}")
        words_list = words_list + f_content
        input("Spied 'Enter' lai turpinātu...")
    
    random_word = choice(words_list)
    if game_menu_answer == 1:
        result = invoke_hangman(random_word, failed_guess_count)

        if result:
            guessed_words.append(random_word)
            win = win + 1
        else:
            loss = loss + 1
            words_list.pop(words_list.index(random_word))