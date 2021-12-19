import random
from verb_world import *

experience_wallet = 75

def log_in(name, occupation, password):
    print("In order to proceed to the next level, you will need to log in again.")
    while True:
        log_in_name = input("Please enter your name. ")
        if log_in_name == name:
            print("Authentication for name complete.")
            break
        else:
            print("Incorrect, please try again.")

    while True:
        log_in_occupation = input("Please enter your occupation. ")
        if log_in_occupation == occupation:
            print("Authentication for occupation complete.")
            break
        else:
            print("Incorrect, please try again.")
    while True:
        log_in_password = input("Please enter your password. ")
        if log_in_password == password:
            print("Authentication for password complete.")
            break
        else:
            print("Incorrect, please try again.")

def verb_questions_two():
    while True:
        scramble_aprender = "aprender"
        l = list(scramble_aprender)
        random.shuffle(l)
        y = ''.join(l)
        print(f'Unscramble the following verb "{y}"')
        to_learn = input(
            '¿Cómo se dice "to learn" en español? \n Please unscramble the verb. ')
        if to_learn== 'aprender':
            print('Excelente, "to learn" es "aprender" en español.')
            verbs_learned['aprender'] = 'to learn'
            verbs_to_learn.pop('to learn')
            print("Here is your updated dictionary of verbs you learned!", verbs_learned)
            global experience_wallet
            experience_wallet += 20
            print(f"You earned 20 points. You now have {experience_wallet} in your experience wallet.")
            break
        else:
            print('Intenta otra vez, por favor.', to_learn, 'is not "to learn."')
