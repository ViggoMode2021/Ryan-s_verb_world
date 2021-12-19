from verb_world import verbs_to_learn, verbs_learned, verb_questions, experience_wallet
from verb_world_two import log_in, verb_questions_two
import random

class Player:
    def __init__(self, name, occupation, password):
        self.name = name
        self.occupation = occupation
        self.password = password


name = input(
    "Welcome to Ryan's Spanish verb world (mundo de verbos en español)! \nPlease enter your name: ")
print("¡Hola!", name)
occupation = input("What is your occupation?: ")
print(f"Oh wow, {name} your job is, {occupation}. ¡Es un trabajo fantástico!")
while True:
    password = input("Lastly, please create a secure password: ")
    if not any(char.isdigit() for char in password) and not any(char.isupper() for char in password):
        print('Password should have at least one numeral or one uppercase letter.')
    else:
        break
print('This is the game menu that will be referenced throughout. Press 1 or 2 to check the dictionaries, '
      '\n press 3 to check your experience wallet or any other key to continue.')
while True:
    menu = int(input(
        '1: Dictionary of verbs you will learn in this game. 2. Verbs you have learned in this game.\n'
        ' 3. Experience wallet. Misc. key. Continue: '))
    if menu == 1:
        print(verbs_to_learn)
    if menu == 2:
        print(verbs_learned, "You haven't learned any verbs yet!")
    if menu == 3:
        print(f"You have {experience_wallet} in your experience wallet.")
    else:
        break
print("When you learn a verb, the verb you learned will be added to your dictionary (#2) \n"
      "and removed from the dictionary of verbs you will learn (#1). Also, you will receive points \n"
      "for each correct answer. They will be added to your experience wallet.")

print("Muy bien, empezamos ahora. Write your answers and submit using the enter key.")

verb_questions()

print("Now, we will continue onto the next level where you will learn the remaining six verbs.")

log_in(name, occupation, password)

verb_questions_two()

game_player = Player(name, occupation, password)
