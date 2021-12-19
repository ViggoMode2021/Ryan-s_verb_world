# list is empty at start of game and a verb is added here once the player learns it.
verbs_learned = {}

verbs_to_learn = {'to talk': '', 'to eat': '', 'to write': '',
                  'to work': '', 'to learn': '', 'to live': ''}

experience_wallet = 0

# function below runs through the verb questions in the game.

def verb_questions():
    while True:
        to_talk = input(
            '¿Cómo se dice "to talk" en español? \n opciones: hablar, comer, escribir ')
        if to_talk == 'hablar':
            print('Excelente, "to talk" es "hablar" en español.')
            verbs_learned['hablar'] = 'to talk'
            verbs_to_learn.pop('to talk')
            print("Here is your updated dictionary of verbs you learned!", verbs_learned)
            global experience_wallet
            experience_wallet += 10
            print(f"You earned 10 points. You now have {experience_wallet} in your experience wallet.")
            break
        else:
            print('Intenta otra vez, por favor.', to_talk, 'is not "to talk"')

    print('Excelente. Notice that the verb "hablar" ends in an "ar". \n In Spanish, we call this an -ar verb.')

    while True:
        to_eat = input(
            '¿Cómo se dice "to eat" en español? \n opciones: hablar, comer, escribir ')
        if to_eat == 'comer':
            print('Excelente, "to eat" es "comer" en español.')
            verbs_learned['comer'] = 'to eat'
            verbs_to_learn.pop('to eat')
            print("Here is your updated dictionary of verbs you learned!", verbs_learned)
            experience_wallet += 10
            print(f"You earned another 10 points. You now have {experience_wallet} in your experience wallet.")
            break
        else:
            print('Intenta otra vez, por favor.', to_eat, 'is not "to eat"')

    print('Excelente. Notice that the verb "comer" ends in an "er". \n In Spanish, we call this an -er verb.')

    while True:
        to_write = input(
            '¿Cómo se dice "to write" en español? \n opciones: hablar, comer, escribir ')
        if to_write == 'escribir':
            print('Excelente, "to write" es "comer" en español.')
            verbs_learned['escribir'] = 'to write'
            verbs_to_learn.pop('to write')
            print("Here is your updated dictionary of verbs you learned!", verbs_learned)
            experience_wallet += 10
            print(f"You earned yet another 10 points. You now have {experience_wallet} in your experience wallet.")
            break
        else:
            print('Intenta otra vez, por favor.',
                  to_write, 'is not "to write"')

    print('Increíble, now we should put them into practice with a quick quiz. \n But first, we will revisit the menu.')
    while True:
        menu = int(input(
            '1: Dictionary of verbs you will learn in this game. 2. Verbs you have learned in this game.\n'
            ' 3. Experience wallet. Misc. key. Continue: '))
        if menu == 1:
            print("Here are the verbs left to learn", verbs_to_learn)
        if menu == 2:
            print("Here are the verbs you have learned", verbs_learned)
        if menu == 3:
            print(f"You have {experience_wallet} in your experience wallet.")
        else:
            break

    print("Write the correct verb in order to complete the statement according to context. \n These sentences will contain cognates, words that are identical in two languages.")

    while True:
        to_eat_question = input(
            'Me gusta ____________ la hamburguesa y las papas fritas. ')
        if to_eat_question == "comer":
            print(
                f'Correcto, the answer is: "Me gusta {to_eat_question} la hamburguesa y las papas fritas.')
            print('I like to eat the hamburger and the french fries.')
            experience_wallet += 15
            print(f"You are awarded 15 points. You now have {experience_wallet} in your experience wallet.")
            break
        else:
            print('Incorrecto. Trata de nuevo por favor.')
    while True:
        to_write_question = input(
            'Para el autor, Stephen King, es importante ________________ mucho. ')
        if to_write_question == "escribir":
            print(
                f'Para el autor, Stephen King, es importante {to_write_question} mucho.')
            print('For the author, Stephen King, it is important to write a lot.')
            experience_wallet += 15
            print(f"You are awarded another 15 points. You now have {experience_wallet} in your experience wallet.")
            break
        else:
            print('Incorrecto. Trata de nuevo por favor.')

    while True:
        to_talk_question = input(
            '¿Te gusta __________ por teléfono? ')
        if to_talk_question == "hablar":
            print(
                f'¿Te gusta {to_talk_question} mucho?')
            print('Do you like to talk on the phone a lot?')
            experience_wallet += 15
            print(f"You are awarded yet another 15 points. You now have {experience_wallet} in your experience wallet.")
            break
            return experience_wallet
        else:
            print('Incorrecto. Trata de nuevo por favor.')
