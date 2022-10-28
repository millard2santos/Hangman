import random
from words import word_list
from stages import logo, stages


word = random.choice(word_list)
list_of_word = []
win = []
lives = 7

for i in word:
    list_of_word.append("_")
for i in word:
    win.append(i)
print(logo)
input("Welcome to Hangman!! Press any key to start")
while list_of_word != win and lives != 0:
    print(f"You have {lives} left!!\n")
    user = input("Guess a letter: \n")
    for i in range(len(win)):
        if user == win[i]:
            list_of_word[i] = user
    if user not in word:
        
        lives -= 1
        
    

    print(stages[lives - 1])
    print(list_of_word)
    
if list_of_word == win:
    print("You win!!!")
else:
    print("You lose")

# while win == False:
#     user_guess = input("Adivina la palabra!! Escoge una letra: ").lower()

#     for i in list_of_word:
#         if user_guess == word[i]:
#             list_of_word[i] == user_guess
    





