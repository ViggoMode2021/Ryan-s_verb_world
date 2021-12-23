from verb_world import verbs_to_learn, verbs_learned, verb_questions # module, variable, and function for set 1 of verb questions
from verb_world_two import log_in, verb_questions_two  # module and functions for set 2 of verb questions
from prizes import *  # module for 'end of game prizes' functionality

class Player: # consruct class for player of game.
    def __init__(self, name, occupation, password):
        self.name = name # player name as input by 'name' variable below
        self.occupation = occupation # player occupation as input by 'occupation' variable below
        self.password = password # player password as input by 'password' variable below

name = input(
    "Welcome to Ryan's Spanish verb world (mundo de verbos en español)! \nPlease enter your name: ")
print("¡Hola!", name)
occupation = input("What is your occupation?: ")
print(f"Oh wow, {name} your job is, {occupation}. ¡Es un trabajo fantástico!")

while True: # loop to check password strength with if statements, len, and isalpha functions
    password = input("Lastly, please create a secure password (between 5 and 10 characters \nand must contain letters.): ")
    if len(password) < 5:
        print("Requested password length is shorter than 5 characters.")
    elif len(password) > 10:
        print("Requested password length is longer than 10 characters.")
    elif not password.isalpha():
        print("Requested password must not contain numbers.")
    else:
        break
print('This is the game menu that will be referenced throughout. Press 1 or 2 to check the dictionaries, '
      '\n press 3 to check your experience wallet or any other key to continue.')

while True: # display game menu
    menu = int(input(
        '1: Dictionary of verbs you will learn in this game. 2. Verbs you have learned in this game.\n'
        ' 3. Experience wallet. Misc. key. Continue: '))
    if menu == 1:
        print(verbs_to_learn) # dictionary of verbs to learn in game, defined in module verb_world
    if menu == 2:
        print(verbs_learned, "You haven't learned any verbs yet!") # dictionary of verbs learned in game, defined in module verb_world
    if menu == 3:
        print(f"You have {experience_wallet} in your experience wallet.") # exp wallet initally set to zero, defined in module verb_world
    else:
        break

print("When you learn a verb, the verb you learned will be added to your dictionary (#2) \n"
      "and removed from the dictionary of verbs you will learn (#1). Also, you will receive points \n"
      "for each correct answer. They will be added to your experience wallet. Please type all answers \n"
      "to questions in lower-case.")

print("Muy bien, empezamos ahora. Write your answers and submit using the enter key.")

verb_questions() # function called from verb_world module

print("Now, we will continue onto the next level where you will learn the remaining three verbs.")

log_in(name, occupation, password) # function called from verb_world_two module

verb_questions_two() # function called from verb_world_two module

print("¡Felicitaciones! You have just completed Ryan's Spanish verb game! You can now use the \n"
      "points in your experience wallet to purchase yourself a trip to these countries: ")

travel_selection(travel_prizes) # function called from prizes module

print("Gracias for playing! ¡Adiós!")

game_player = Player(name, occupation, password) # instance of 'class Player' defined above
