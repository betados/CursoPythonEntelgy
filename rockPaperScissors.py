#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

moves = ['rock', 'paper', 'scissors']

done = False
while not done:
    print('\n\n')
    gameMove = moves[random.randrange(len(moves))]
    userMove = input("Make your move:")

    if userMove == 'exit':
        done = True
        break

    if userMove not in moves:
        continue

    print("Computers move is: " + gameMove)
    if gameMove == userMove:
        print('DRAW!')
        continue
git 
    gameIndex = moves.index(gameMove)
    userIndex = moves.index(userMove)
    lista = [gameIndex, userIndex]

    if max(lista) == len(moves)-1 and min(lista) == 0:
        winner = 0
    else:
        winner = max(lista)

    if gameMove == moves[winner]:
        print("Machine wins!")
    else:
        print("YOU win!")



