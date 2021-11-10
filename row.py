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

n = 0
while n < 2000:
 n = n + 1
 row_input()
 row_input2()
 row_input3()