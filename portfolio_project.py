from verb_world import verbs_to_learn, verbs_learned, verb_questions


class Player:
    def __init__(self, name, occupation, password):
        self.name = name
        self.occupation = occupation
        self.password = password


name = input(
    "Welcome to Ryan's Spanish verb world (mundo de verbos en español)! \nPlease enter your name: ")
print("¡Hola!", name)
occupation = input("What is your occupation?: ")
print("Oh wow, your job is", occupation, '¡es un trabajo fantástico!')
while True:
    password = input("Lastly, please create a secure password: ")
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral and one uppercase letter.')
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter and one number')
    else:
        break
print('This is the game menu that will be referenced throughout. Press 1 or 2 to check the dictionary or any other key to continue.')
while True:
    menu = int(input(
        '1: Check dictionary of verbs you will learn in this game. 2. Verbs you have learned in this game.: '))
    if menu == 1:
        print(verbs_to_learn)
    if menu == 2:
        print(verbs_learned, "You haven't learned any verbs yet!")
    if menu == 3:
        break
print("Muy bien, empezamos ahora. Write your answers and submit using the enter key.")
verb_questions()


game_player = Player(name, occupation, password)
