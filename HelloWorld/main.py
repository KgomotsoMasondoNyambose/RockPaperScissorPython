# import random
#
# print(random.random(1, 10))

# from datetime import timedelta

# delta = timedelta(
#     days = 50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )

# print(timedelta(days=64, seconds=29156, microseconds=10))

import random

members = ['Scissor', 'Rock', 'Paper']

player_one_name = input('Player 1 enter your name: ')
player_two_name = input('Player 2 enter your name: ')
play = ''

while play != 'No'.upper():
    play = input('Press enter to play or no to quit').upper()
    
    player1 = random.choice(members)
    player2 = random.choice(members)
    if player1 == members[0] and player2 == members[2]:
        print(f'{player_one_name} wins, {player_one_name}: {player1}, {player_two_name}: {player2}  ')
    elif player2 == members[0] and player1 == members[2]:
        print(f'{player_two_name} wins, {player_one_name}: {player1}, {player_two_name}: {player2}  ')
    elif player1 == members[2] and player2 == members[1]:
        print(f'{player_one_name} wins, {player_one_name}: {player1}, {player_two_name}: {player2}  ')
    elif player2 == members[2] and player1 == members[1]:
        print(f'{player_two_name} wins, {player_one_name}: {player1}, {player_two_name}: {player2}  ')
    elif player1 == members[1] and player2 == members[0]:
        print(f'{player_one_name} wins, {player_one_name}: {player1}, {player_two_name}: {player2}  ')
    elif player2 == members[1] and player1 == members[0]:
        print(f'{player_two_name} wins, player1 = {player_one_name}: {player1}, player2 = {player_two_name}: {player2}  ')
    else:
        print(f'Draw game:{player_one_name} :{player1}, {player_two_name} :{player2}')
# else:
#     play = input('Do you still wanna play (yes or no)').upper()
