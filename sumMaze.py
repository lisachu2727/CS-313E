#File: sumMaze.py
#Description: HW 8
#Student's Name: Lisa Chu
#Student's UT EID: tc29328
#Course Name: CS 313E
#Unique Number: 50739
#
#Date Created: 4/18/19
#Date Last Modified: 4/19/19

#Importing copy to make copy of maze

import copy

#Defining state class that describes current position, history of moves, and
#sum of moves

class State:
    def __init__(self, grid, history, startRow, startCol, total):
        self.grid = grid
        self.history = history
        self.startRow = startRow
        self.startCol = startCol
        self.total = total

    def __str__(self):
        string = '   Grid:'
        
        for row in self.grid:
            string += '\n      '
            for number in row:
                string += str(number).ljust(5)

        string += '\n   History: ' + str(self.history)
        string += '\n   Start point: (' + str(self.startRow) + ',' + \
                  str(self.startCol) + ')'
        string += '\n   Sum so far: ' + str(self.total)
        string += '\n'
 
        return string
            
#Checks to see if move is within the maze and has not been visited

def isValid(grid, gridRows, gridCols, row, col):
    if row < 0 or row >= gridRows or col < 0 or col >= gridCols:
        return False

    if grid[row][col] == 'X':
        return False

    return True

#Finds path through a maze of integers using depth-first search

def solve(state, targetValue, endRow, endCol, gridRows, gridCols):
    print('Is this a goal state?')

    #Checks to see if current state is goal state
    
    if state.startRow == endRow and state.startCol == endCol and \
       state.total == targetValue:
        print('Solution found!')
        return state.history

    #Checks to see if target sum has been exceeded
    
    if state.total > targetValue:
        print('No. Target exceeded: abandoning path')
        return None

    else:

        #Move right if moving right is a valid move
        
        print('No. Can I move right?')
        if isValid(state.grid, gridRows, gridCols, state.startRow, \
                   state.startCol + 1):
            print('Yes! Moving right.')
            print()

            #Calculates variables for the new state and creates new state

            newRow = state.startRow
            newCol = state.startCol + 1
            
            newGrid = copy.deepcopy(state.grid)
            newGrid[newRow][newCol] = 'X'

            newPosition = state.grid[newRow][newCol]
            
            newHistory = state.history[:]
            newHistory.append(newPosition)
            
            newTotal = state.total + newPosition
            
            newState = State(newGrid, newHistory, newRow, newCol, newTotal)

            #Print out updated maze
            
            print('Problem is now:')
            print(newState)

            #Continue solving maze
            
            result = solve(newState, targetValue, endRow, endCol, gridRows, \
                           gridCols)
         
            if result != None:
                return result
            
        #Move up if moving up is a valid move

        print('No. Can I move up?')
        if isValid(state.grid, gridRows, gridCols, state.startRow - 1, \
                   state.startCol):
            print('Yes! Moving up.')
            print()

            #Calculates variables for the new state and creates new state
            
            newRow = state.startRow - 1
            newCol = state.startCol
            
            newGrid = copy.deepcopy(state.grid)
            newGrid[newRow][newCol] = 'X'

            newPosition = state.grid[newRow][newCol]
            
            newHistory = state.history[:]
            newHistory.append(newPosition)
            
            newTotal = state.total + newPosition
            
            newState = State(newGrid, newHistory, newRow, newCol, newTotal)

            #Print out updated maze
            
            print('Problem is now:') 
            print(newState)

            #Continue solving maze
            
            result = solve(newState, targetValue, endRow, endCol, gridRows, \
                           gridCols)
           
            if result != None:
                return result

        #Move down if moving down is a valid move

        print('No. Can I move down?')
        if isValid(state.grid, gridRows, gridCols, state.startRow + 1, \
                   state.startCol):
            print('Yes! Moving down.')
            print()

            #Calculates variables for the new state and creates new state

            newRow = state.startRow + 1
            newCol = state.startCol
            
            newGrid = copy.deepcopy(state.grid)
            newGrid[newRow][newCol] = 'X'

            newPosition = state.grid[newRow][newCol]
            
            newHistory = state.history[:]
            newHistory.append(newPosition)
            
            newTotal = state.total + newPosition
            
            newState = State(newGrid, newHistory, newRow, newCol, newTotal)

            #Print out updated maze
            
            print('Problem is now:')
            print(newState)

            #Continue solving maze
            
            result = solve(newState, targetValue, endRow, endCol, gridRows, \
                           gridCols)
          
            if result != None:
                return result

        #Move left if moving left is a valid move

        print('No. Can I move left?')
        if isValid(state.grid, gridRows, gridCols, state.startRow, \
                   state.startCol - 1):
            print('Yes! Moving left.')
            print()

            #Calculates variables for the new state and creates new state

            newRow = state.startRow
            newCol = state.startCol - 1
            
            newGrid = copy.deepcopy(state.grid)
            newGrid[newRow][newCol] = 'X'

            newPosition = state.grid[newRow][newCol]
            
            newHistory = state.history[:]
            newHistory.append(newPosition)
            
            newTotal = state.total + newPosition
            
            newState = State(newGrid, newHistory, newRow, newCol, newTotal)

            #Print out updated maze

            print('Problem is now:')
            print(newState)
            
            #Continue solving maze

            result = solve(newState, targetValue, endRow, endCol, gridRows, \
                           gridCols)
          
            if result != None:
                return result

        print("Couldn't move in any direction. Backtracking.")
        return None
    
def main():
    file = open('mazedata.txt', 'r')            
    grid = []                                   #List to store maze data
    
    line = file.readline().split()              #Read first line

    #Store first line into integer variables
    
    targetValue, gridRows, gridCols, startRow, startCol, endRow, endCol = \
                 list(map(int, line))           

    #Read rest of file and store in grid list
    
    for line in file:
        line = line.strip()
        line = line.split(' ')
        rows = list(map(int, line))
        grid.append(rows)
        
    file.close()

    #Set inital position
    position = [grid[startRow][startCol]]
    grid[startRow][startCol] = 'X'
    initialState = State(grid, position, startRow, startCol, sum(position))

    print(initialState)

    print(solve(initialState, targetValue, endRow, endCol, gridRows, gridCols))
        
main()
