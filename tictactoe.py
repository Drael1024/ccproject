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

def calculatePossibleMoves(): # Creates and returns a list which has all the empty (and non-0th) field numbers
    possibilities = []
    for x, letter in enumerate(table):
        if letter == ' ' and x != 0:
            possibilities.append(x)
    return possibilities

def AI():
    possibleMoves = calculatePossibleMoves() # Getting "possible" (empty) positions.
    move = 0 # This won't be changed if there is no empty positions!! It also means the game ends in a draw! Check the main() function about it.

    for letter in ['O', 'X']: #Trying out moves for both smybols. First the AI tries to win and then tries to "counter-play".
        for i in possibleMoves:
            testTable = table[:] #Clones the current table.
            testTable[i] = letter #Checks all the possible positions.
            if isWinner(testTable, letter): #If the AI puts down an O and wins in a test table, then it's the correct move! Also tries with "X" to see if the player wins, so at the computer's turn, the AI going to put an "O" there to counter-play!
                move = i
                return move

    emptyCorners = [] # Next priorities are the corners.
    for i in possibleMoves: 
        if i in [1,3,7,9]:
            emptyCorners.append(i) 

    if len(emptyCorners) > 0: # Only if it's possible to put a symbol there.
        r = random.randrange(0,len(emptyCorners))
        move = emptyCorners[r]
        return move

    if 5 in possibleMoves: # Next priority is the center square, if possible.
        move = 5
        return move

    emptyEdges = [] # The last priorities are the edges.
    for i in possibleMoves:
        if i in [2,4,6,8]:
            emptyEdges.append(i)
            
    if len(emptyEdges) > 0: # Only if it's possible to put a symbol.
        r = random.randrange(0,len(emptyEdges))
        move = emptyEdges[r]
        
    return move # When there are no possibilites left, the AI puts a symbol at the 0th index! It means the game is over and it's a draw!

def main():
    showTable(table)

    while (' ' in table):
        if not(isWinner(table, 'O')):
            playerTurn()
            showTable(table)
        else:
            print('You lost... (╥﹏╥)')
            break
        if not(isWinner(table, 'X')):
            move = AI()
            if move == 0:
                print('Draw! ( ͡° ͜ʖ ͡°)')
                break
            else:
                time.sleep(1)
                placeLetter('O', move)
                showTable(table)
        else:
            print('You won! \(ˆ˚ˆ)/ ')
            break
    else:
        print('Draw! ( ͡° ͜ʖ ͡°)')

main()