from random import choice

player_id = input('What is your name: \t')
print(f'Welcome {player_id} to my game of Rock, Paper, Scissors.\n')
replay = False

while replay == False:

    optional_choices = ['R', 'P', 'S']
    player_choice = (input("\nWhat will be your choice: \n1. R for Rock.\n2. P for paper.\n3. S for scissors. \t"))
    computer_choice = choice(optional_choices)

    #The next line of code is to prevent error due to letter's case from input
    player_choice = player_choice.upper()


    if player_choice == "R":
        if computer_choice == "P": 
            print(f'\n{player_id}(Rock):CPU(Paper)')
            print('Paper covers Rock, Computer wins.')
        else: 
            print(f'\n{player_id}(Rock):CPU(Scissors)')
            print(f"Rock smashes Scissors, {player_id} wins.")
    elif player_choice == "P":
        if computer_choice == "R":
            print(f'\n{player_id}(Paper):CPU(Rock)')
            print(f'Paper covers Rock, {player_id} wins.')
        else:
            print(f'\n{player_id}(Paper):CPU(Scissors)')
            print("Scissors cuts Paper, Computer wins.")
    elif player_choice == "S":
        if computer_choice == "R":
            print(f'\n{player_id}(Scissors):CPU(Rock)')
            print("Rock smashes Scissors, Computer wins.")
        else:
            print(f'\n{player_id}(Scissors):CPU(Paper)')
            print(f"Scissors cuts Paper, {player_id} wins.")
    elif player_choice == computer_choice:
        print("\nIt is a tie...")
    else:
        print('\nInvalid input...')

    Replay= input("\nWould you like to play again: \ny/n: \t")
    if Replay == "y":
        replay = False
        print("\nLet's make another round...")
    else:
        print('\nThanks for playing, pls drop positive reviews..')
        break


