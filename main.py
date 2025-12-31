#        ____                                      
#       / __ \_________  ____ __________ _____ ___ 
#      / /_/ / ___/ __ \/ __ `/ ___/ __ `/ __ `__ \
#     / ____/ /  / /_/ / /_/ / /  / /_/ / / / / / /
#    /_/   /_/   \____/\__, /_/   \__,_/_/ /_/ /_/ 
#       ____ ___  ____/____// /__     / /_  __  __ 
#      / __ `__ \/ __ `/ __  / _ \   / __ \/ / / / 
#     / / / / / / /_/ / /_/ /  __/  / /_/ / /_/ /  
#    /_/ /_/ /_/\__,_/\__,_/\___/  /_.___/\__, /   
#       _____                            /____/    
#      / ___/____ _______   _____  _____/ /_       
#      \__ \/ __ `/ ___/ | / / _ \/ ___/ __ \      
#     ___/ / /_/ / /   | |/ /  __(__  ) / / /      
#    /____/\__,_/_/    |___/\___/____/_/ /_/       
#                                                                           

import random
import sys

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



user_word = ""
user_word_spaces = []
attempt = 7

print("Thanksgiving Hangman!")

while True: 
    try:
        file_path = str(input("------------------------------------------\nEnter the path of your .txt file of your wordbank (just type demo.txt): ")) #find and read path
        with open(file_path, "r", encoding="utf-8") as f:
            wordbank_data = f.read()
        break
    except:
        print("Error! That is not a valid path or your file type isn't a .txt!")
        continue
    

wordbank_list = wordbank_data.split('\n') 

#print(wordbank_list)
for i in range(len(wordbank_list)):
    new_word = ""
    
    for character in wordbank_list[i]:
        if character != " ":
            new_word = new_word + character
    
    wordbank_list[i] = new_word


user_word = random.choice(wordbank_list).lower()



for i in range(len(user_word)):
    user_word_spaces.append("_ ")



while True:
    print("------------------------------------------")
    print(HANGMANPICS[7 - attempt])
    print("".join(user_word_spaces))
    
    while True:
        user_letter_input = input("\nEnter a letter: ")
        user_letter_input = user_letter_input.strip()
        user_letter_input = user_letter_input.lower()
    
        if len(user_letter_input) != 1:
            print("Please enter 1 letter!")
            continue
        if user_letter_input == "":
            print("Type in a letter!")
            continue
        if user_letter_input in "".join(user_word_spaces):
            print("You already know that letter is in the word!")
            continue
        
        
        break
    
    user_word_list = list(user_word)
    
    #count = -1
    position = []
    
    if user_letter_input in user_word:
        for i in range(len(user_word_list)):
            if user_word_list[i] == user_letter_input:
                position.append(i)
        for j in range(len(position)):
            user_word_spaces[position[j]] = user_letter_input
        
        if user_word == "".join(user_word_spaces):
            print("------------------------------------------\nYou win!")
            sys.exit()
    
    
    
    else:
        attempt = attempt - 1
        if attempt == 0:
            print("------------------------------------------\nYou lost!")
            sys.exit()
        print("That letter is not in the word!")
        print("You have "+ str(attempt) +" tries remaining")
