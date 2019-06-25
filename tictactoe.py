table = [' ' for x in range(10)] # Creating the table for the game. (Note: We won't use the 0th element!!!)

def showTable():
    print(' ' + table[1] + ' | ' + table[2] + ' | ' + table[3])
    print('-----------')
    print(' ' + table[4] + ' | ' + table[5] + ' | ' + table[6])
    print('-----------')
    print(' ' + table[7] + ' | ' + table[8] + ' | ' + table[9])

def placeLetter(letter, position): # Inserts the given symbol into the given position.
    table[position] = letter

def spaceIsFree(position): # Tells you if it's available to put down your symbol or not.
    if table[position] == ' ':
        return True
    else:
        return False