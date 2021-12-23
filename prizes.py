# below is a list of places the player can purchase with what they have from their experience wallet
travel_prizes = ['Argentina - 200 experience', 'Colombia - 170 experience', 'Mexico - 160 experience', 'Peru - 190 experience', 'Ecuador - 180 experience']

experience_wallet = 210 # final amount before player makes a purchase
# function for player to choose a prize at end of game
def travel_selection(travel_prizes):
      for prize in travel_prizes: # for loop to iterate and show the prizes in the list above
            print(prize)

      global experience_wallet
      print(f'You have {experience_wallet} in your experience wallet. Where would you like to purchase your trip to? ')

      prize_selector = int(input("1. Press 1 if you want to save your experience. 2. Press 2 to choose your own from the list. "))

      while True: # allows player to leave game without picking a prize
            if prize_selector == 1:
                  print("Okay, we hope to see you in the next game!")
                  break

            if prize_selector == 2: # allows player to input their prize
                  prize_selector_choose = input('Where would you like to go? ')
                  if prize_selector_choose == 'Argentina':
                        experience_wallet -= 200
                        print(f'You now have {experience_wallet} in your experience wallet. Fun fact: Argentina has the most European ancestary of any Latin American country.')
                        break
                  if prize_selector_choose == 'Colombia':
                        experience_wallet -= 170
                        print(f'You now have {experience_wallet} in your experience wallet. Fun fact: Salentó, in the Quindío region, has the tallest palm trees in the world.')
                        break
                  if prize_selector_choose == 'Mexico':
                        experience_wallet -= 160
                        print(f'You now have {experience_wallet} in your experience wallet. Fun fact: The caesar salad was invented in Tijuana by Caesar Cardini, an Italian chef.')
                        break
                  if prize_selector_choose == 'Ecuador':
                        experience_wallet -= 180
                        print(f'You now have {experience_wallet} in your experience wallet. Fun fact: "Quito is the second highest capital city in terms of elevation (9350 ft above sea level)')
                        break
                      
                  if prize_selector_choose == 'Peru':
                        experience_wallet -= 180
                        print(f'You now have {experience_wallet} in your experience wallet. Fun fact: Huacachina is the only natural oasis in South America.')
                        break
                  else:
                       print("Please accurately type the country's name from the list!")
