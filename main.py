import numpy as np

board = np.zeros(shape = (10,10), dtype = int)

print(board)

row = [9]*10




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
    











n = 0
while n < 2000:
 n = n + 1
 win_checker_verticle()
 row_input()
 row_input2()
 row_input3()
 



