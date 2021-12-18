# list is empty at start of game and a verb is added here once the player learns it.
verbs_learned = {}

verbs_to_learn = {'to talk': '', 'to eat': ''}


# function below runs through the verb questions in the game.

def verb_questions():
    while True:
        to_talk = input(
            '¿Cómo se dice "to talk" en español? \n opciones: bailar, hablar, comer ')
        if to_talk == 'hablar':
            print('Excelente, "to talk" es "hablar" en español.')
            verbs_learned['hablar'] = 'to talk'
            print("Here is your updated dictionary of verbs you learned!",verbs_learned)
            break
        else:
            print('Intenta otra vez, por favor.')
    print('Continuamos.')
    # while True:
