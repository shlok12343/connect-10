import numpy as np

board = np.zeros(shape = (10,10), dtype = int)

print(board)

row = [9]*10

win = False


def row_input():
  player_input = int(input("row number -- "))
  player_input = player_input - 1
  valid_enteries = [i for i in range(11)]
  while player_input not in valid_enteries:
    print("choose from rows 1 to 10 ")
    player_input = int(input("row number -- "))
    

  
  board[row[player_input]][player_input] = 1
  print(board)

  if row[player_input] == -1:
   valid_enteries.pop(player_input)
  else:
   row[player_input] = row[player_input] - 1

def row_input2():
  player_input2 = int(input("row number -- "))
  player_input2 = player_input2 - 1
  valid_enteries = [i for i in range(11)]
  while player_input2 not in valid_enteries:
    print("choose from rows 1 to 10 ")
    player_input2 = int(input("row number -- "))
    

  
  board[row[player_input2]][player_input2] = 2
  print(board)

  if row[player_input2] == -1:
   valid_enteries.pop(player_input2)
  else:
   row[player_input2] = row[player_input2] - 1

def row_input3():
  player_input3 = int(input("row number -- "))
  player_input3 = player_input3 - 1
  valid_enteries = [i for i in range(11)]
  while player_input3 not in valid_enteries:
    print("choose from rows 1 to 10 ")
    player_input3 = int(input("row number -- "))
    

  
  board[row[player_input3]][player_input3] = 3
  print(board)

  if row[player_input3] == -1:
   valid_enteries.pop(player_input3)
  else:
   row[player_input3] = row[player_input3] - 1


def win_checker_verticle():
  for j in range(0,10):
    for i in range(0,7):
      if board[i][j]  == 1 and board[i+1][j] == 1 and board[i+2][j] == 1 and board[i+3][j] == 1:
        print("win")
      elif board[i][j] == 2 and board[i+1][j] == 2 and board[i+2][j] == 2 and board[i+3][j] == 2:
        print("win")
      elif board[i][j] == 3 and board[i+1][j] == 3 and board[i+2][j] == 3 and board[i+3][j] == 3:
        print("win")

def win_checker_horizontal():
  
  for j in range(0,7):
    for i in range(0,10):
      if board[i][j]  == 1 and board[i][j+1] == 1 and board[i][j+2] == 1 and board[i][j+3] == 1:
        print("win")
      elif board[i][j] == 2 and board[i][j+1] == 2 and board[i][j+2] == 2 and board[i][j+3] == 2:
        print("win")
      elif board[i][j] == 3 and board[i][j+1] == 3 and board[i][j+2] == 3 and board[i][j+3] == 3:
        print("win")

def win_checker_counter_diagnal():
  
  for j in range(0,7):
    for i in range(0,7):
      if board[i][j]  == 1 and board[i+1][j+1] == 1 and board[i+2][j+2] == 1 and board[i+3][j+3] == 1:
        print("win")
      elif board[i][j] == 2 and board[i+1][j+1] == 2 and board[i+1][j+2] == 2 and board[i+1][j+3] == 2:
        print("win")
      elif board[i][j] == 3 and board[i+1][j+1] == 3 and board[i+2][j+2] == 3 and board[i+3][j+3] == 3:
        print("win")

def win_checker_diagnal():
  
  for j in range(0,7):
    for i in reversed(range(3,10)):
      if board[i][j]  == 1 and board[i-1][j+1] == 1 and board[i-2][j+2] == 1 and board[i-3][j+3] == 1:
        print("win")
        
      elif board[i][j] == 2 and board[i-1][j+1] == 2 and board[i-2][j+2] == 2 and board[i-3][j+3] == 2:
        print("win")
      elif board[i][j] == 3 and board[i-1][j+1] == 3 and board[i-2][j+2] == 3 and board[i-3][j+3] == 3:
        print("win")
    











n = 0
while n < 2000:
 n = n + 1


 row_input()
 win_checker_horizontal()
 win_checker_verticle()
 win_checker_diagnal()
 win_checker_counter_diagnal()
   
 row_input2()
 win_checker_horizontal()
 win_checker_verticle()
 win_checker_diagnal()
 win_checker_counter_diagnal()

 row_input3()
 win_checker_horizontal()
 win_checker_verticle()
 win_checker_diagnal()
 win_checker_counter_diagnal()
