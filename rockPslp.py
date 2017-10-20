#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']

done = False
while not done:
    print('\n\n')
    gameMove = moves[random.randrange(len(moves))]
    userMove = input("Play your move:")

    if userMove not in moves:
        continue

    if userMove == 'exit':
        break

    print("Computers move is: " + gameMove)
    if gameMove == userMove:
        print('DRAW!')
        continue

    gameIndex = moves.index(gameMove)
    userIndex = moves.index(userMove)
    lista = [gameIndex, userIndex]

    if max(lista) == len(moves) - 1 and min(lista) == 0:
        winner = 0
    else:
        winner = max(lista)

    if gameMove == moves[winner]:
        print("Ha ganado la máquina")
    else:
        print("Has ganado")