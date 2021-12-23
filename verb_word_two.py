import random # used below
from verb_world import * # used to import dictionaries

experience_wallet = 75 # variable reset here as 75 because it was easier than to import it

def log_in(name, occupation, password): # log-in authentication for player to log-in again after completing level 1
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

# function below is for second set of verb questions
def verb_questions_two():
    while True:
        scramble_aprender = "aprender" # this is the correct verb answer
        l = list(scramble_aprender) # functionality to scramble string above for player to unscramble
        random.shuffle(l) # functionality to scramble string above for player to unscramble
        y = ''.join(l) # functionality to scramble string above for player to unscramble
        print(f'Unscramble the following verb "{y}" Hint: it is an -er verb, meaning it ends in -er.')
        to_learn = input(
            '¿Cómo se dice "to learn" en español? \n Please unscramble the verb. ')
        if to_learn == 'aprender':
            print('Excelente, "to learn" es "aprender" en español.')
            verbs_learned['aprender'] = 'to learn'
            verbs_to_learn.pop('to learn')
            print("Here is your updated dictionary of verbs you learned!", verbs_learned)
            global experience_wallet
            experience_wallet += 20
            print(
                f"You earned 20 points. You now have {experience_wallet} in your experience wallet.")
            break
        else:
            print('Intenta otra vez, por favor.',
                  to_learn, 'is not "to learn."')

    while True:
        scramble_trabajar = "trabajar"
        l = list(scramble_trabajar)
        random.shuffle(l)
        y = ''.join(l)
        print(f'Unscramble the following verb "{y}" Hint: it is an -ar verb, meaning it ends in -ar.')
        to_work = input(
            '¿Cómo se dice "to work" en español? \n Please unscramble the verb. ')
        if to_work == 'trabajar':
            print('Por supuesto, "to work" es "trabajar" en español.')
            verbs_learned['trabajar'] = 'to work'
            verbs_to_learn.pop('to work')
            print("Here is your updated dictionary of verbs you learned!", verbs_learned)
            experience_wallet += 20
            print(
                f"You earned 20 points again, you got money like that?. You now have {experience_wallet} in your experience wallet.")
            break
        else:
            print('Intenta otra vez, por favor.', to_work, 'is not "to work."')

    while True:
        scramble_vivir = "vivir"
        l = list(scramble_vivir)
        random.shuffle(l)
        y = ''.join(l)
        print(f'Unscramble the following verb "{y}" Hint: it is an -ir verb, meaning it ends in -ir.')
        to_live = input(
            '¿Cómo se dice "to live" en español? \n Please unscramble the verb. ')
        if to_live == 'vivir':
            print('Genial, "to live" es "vivir" en español.')
            verbs_learned['vivir'] = 'to live'
            verbs_to_learn.pop('to live')
            print("Here is your updated dictionary of verbs you learned!", verbs_learned)
            experience_wallet += 20
            print(
                f"You earned another whopping 20 points. You now have {experience_wallet} in your experience wallet.")
            break
        else:
            print('Intenta otra vez, por favor.', to_live, 'is not "to live."')

    print('Fantástico, now we will finish with another quiz for the verbs you learned. \n But first, we will revisit the menu.')
    while True:
        menu = int(input(
            '1: Dictionary of verbs you will learn in this game. 2. Verbs you have learned in this game.\n'
            ' 3. Experience wallet. Misc. key. Continue: '))
        if menu == 1:
            print("There are no more verbs left to learn!", verbs_to_learn) # dictionary is empty
        if menu == 2:
            print("Here are the verbs you have learned", verbs_learned) # dictionary is full
        if menu == 3:
            print(f"You have {experience_wallet} in your experience wallet.")
        else:
            break

    print("Write the correct verb in order to complete the statement according to context. \n These sentences will contain cognates, words that are identical in two languages.")

    while True: # some more fill in the blank questions
        to_live_question = input(
            'Yo prefiero ________________ en Colombia en un apartamento. ')
        if to_live_question == "vivir":
            print(
                f'Correcto, the answer is: Yo prefiero {to_live_question} en Colombia en un apartamento.')
            print('I prefer to live in Colombia in an apartment.')
            experience_wallet += 25
            print(f"You are awarded 25 points. You now have {experience_wallet} in your experience wallet.")
            break
        else:
            print('Incorrecto. Trata de nuevo por favor.')

    while True:
        to_learn_question = input(
            'La universidad es buena para _____________ nueva información. ')
        if to_learn_question == "aprender":
            print(
                f'La universidad es buena para {to_learn_question} nueva información.')
            print('The university is good to learn new information.')
            experience_wallet += 25
            print(f"You are awarded another 25 points. You now have {experience_wallet} in your experience wallet.")
            break
        else:
            print('Incorrecto. Trata de nuevo por favor.')

    while True:
        to_work_question = input(
            'En una carrera o profesión, es necesario _____________ muchas horas. ')
        if to_work_question == "trabajar":
            print(
                f'En una carrera o profesión, es necesario {to_work_question} muchas horas.')
            print('In a career or profession, it is necessary to work many hours.')
            experience_wallet += 25
            print(f"You are awarded yet another 25 points. You now have {experience_wallet} in your experience wallet.")
            break
        else:
            print('Incorrecto. Trata de nuevo por favor.')
