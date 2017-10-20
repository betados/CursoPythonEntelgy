#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']

done = False
while not done:
    print('\n\n')
    gameMove = moves[random.randrange(len(moves))]
    userMove = input("Make your move:")

    if userMove == 'exit':
        done = True
        break

    if userMove not in moves:
        print("Escribe bien!")
        continue

    print("Computers move is: " + gameMove)
    if gameMove == userMove:
        print('DRAW!')
        continue

    gameIndex = moves.index(gameMove)
    userIndex = moves.index(userMove)

    i = 0
    while True:
        i += 1
        if moves[gameIndex-i] == userMove:
            break

    if abs(i) % 2 == 0:
        print("Machine wins!")
    else:
        print("YOU win!")
