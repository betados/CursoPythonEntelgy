#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

moves = ['rock', 'lizard', 'spock', 'scissors', 'paper']
while True:
    print('\n\n')
    machineMove = moves[random.randrange(len(moves))]
    userMove = input("Make your move:")

    if userMove == 'exit':
        print('BYE!')
        break

    if userMove not in moves:
        print("¡Escribe bien!")
        continue

    print("Computers move is: " + machineMove)
    if machineMove == userMove:
        print('DRAW!')
        continue

    machineIndex = moves.index(machineMove)

    i = 0
    while moves[machineIndex-i] != userMove:
        i += 1

    if i % 2 == 0:
        print("Machine wins!")
    else:
        print("YOU win!")
