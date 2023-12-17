#!/usr/bin/env python
# coding: utf-8

# # Tic-Tac-Toe

# In[22]:


def playerWon(grid):
    '''
    Checks based on grid to see if there is a winner.
    Return true if there is and false otherwise.
    '''
    for i in grid:
        if i[0] == i[1] and i[1] == i[2] and i[2] != 0:
            return True
    for i in range(3):
        if grid[0][i] == grid[1][i] and grid[1][i] == grid[2][i] and grid[2][i] != 0:
            return True
    
    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[2][2] != 0:
        return True
    return False


# In[23]:


def full(grid):
    '''
    Check if grid is completely filled, returning true or false.
    '''
    for i in grid:
        for j in i:
            if j == 0:
                return False
    return True


# In[24]:


def drawGrid(grid):
    '''
    Print out grid.
    '''
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                print("| ",end='')
            elif grid[i][j] == 1:
                print("|x",end='')
            else:
                print("|o",end='')
        print("|")


# In[21]:


# input player names
player1 = input("Player1, enter your name: ")
print("Welcome, " + player1)
player2 = input("Player1, enter your name: ")
print("Welcome, " + player2)


# In[25]:


player = 1
grid = [[0,0,0],[0,0,0],[0,0,0]]

while True:
    drawGrid(grid)
    if player == 1:
        row = int(input(player1 + ", enter the row: "))
        col = int(input(player1 + ", enter the column: "))
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid choice. Please try again.")
            continue
        if grid[row][col] != 0:
            print("Invalid choice. Please try again.")
            continue
        else:
            grid[row][col] = 1
    else:
        row = int(input(player2 + ", enter the row: "))
        col = int(input(player2 + ", enter the column: "))
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid choice. Please try again.")
            continue
        if grid[row][col] != 0:
            print("Invalid choice. Please try again.")
            continue
        else:
            grid[row][col] = 2
            
    # check for winners
    if playerWon(grid):
        if player == 1:
            print("Congratulations, " + player1 + "! You won!")
        else:
            print("Congratulations, " + player2 + "! You won!")
        break
    if full(grid):
        print("Cat's game!")
        break
    if player == 1:
        player = 2
    else:
        player = 1

