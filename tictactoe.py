import random
import os
import time

table = [' ' for x in range(10)] # Creating the table for the game. (Note: We won't use the 0th element!!!)

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def showTable(table): # Prints out the table.
    clear()
    print(' ' + table[7] + ' | ' + table[8] + ' | ' + table[9])
    print('-----------')
    print(' ' + table[4] + ' | ' + table[5] + ' | ' + table[6])
    print('-----------')
    print(' ' + table[1] + ' | ' + table[2] + ' | ' + table[3])

def placeLetter(letter, position): # Inserts the given symbol into the given position.
    table[position] = letter

def spaceIsFree(position): # Tells you if it's available to put down your symbol or not.
    if table[position] == ' ':
        return True
    else:
        return False

def isWinner(tableName, letter): # Win condition checker.
    winCombinations = [
       (1, 2, 3),
       (4, 5, 6),
       (7, 8, 9),
       (1, 4, 7),
       (2, 5, 8),
       (3, 6, 9),
       (1, 5, 9),
       (3, 5, 7),
    ]
    
    for i,j,k in winCombinations: # Iterating through the winCombinations, if there's any match, returns true!
        if (tableName[i] == letter and tableName[j] == letter and tableName[k] == letter):
            return True

def playerTurn(): # :)
    while True:
        try:
            position = int(input('Where do you want to place your cross? (1-9) >>>'))
            if position > 0 and position < 10:
                if spaceIsFree(position): # If it's empty, player can place the symbol.
                    placeLetter('X', position)
                    break
                else: # If it's not, then:
                    print('It\'s not an empty slot, please pick another one!')
            else: # Player input was out of range.
                print('Invalid input! Your number is out of the allowed range!')
        except: # Fool proofing the input. If it can't convert to int, make him redo the procedure!
            print('Invalid input! You must enter a number!')