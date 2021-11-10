def win_checkerup():
  for j in range(0,10):
    for i in range(0,7):
      if board[i][j]  == (1 or 2 or 3):
        print("win")

def win_checker_horizontal():
  for j in range(0,10):
    for i in range(0,7):
      if board[i][j]  == (1 or 2 or 3):
        print("win")


def win_checker_verticle():
  for j in range(10,0):
    for i in range(10,0):
      if board[i][j] and board[i+1][j] and board[i+2][j] and board[i+3][j] == 1:
        print("win")
      elif board[i][j] and board[i+1][j] and board[i+2][j] and board[i+3][j] == 2:
        print("win")
      elif board[i][j] and board[i+1][j] and board[i+2][j] and board[i+3][j] == 3:
        print("win")

def win_checker_verticle():
  for j in range(0,10):
    for i in range(0,7):
      if board[i][j] and board[i+1][j] and board[i+2][j] and board[i+3][j] == 1:
        print("win")
      elif board[i][j] and board[i+1][j] and board[i+2][j] and board[i+3][j] == 2:
        print("win")
      elif board[i][j] and board[i+1][j] and board[i+2][j] and board[i+3][j] == 3:
        print("win")

def win_checker_verticle():
  for j in range(0,10):
    for i in range(0,7):
      if board[i][j]  == 1 and board[i+1][j] == 1 and board[i+2][j] == 1 and board[i+3][j] == 1:
        print("win")
      elif board[i][j] == 2 and board[i+1][j] == 2 and board[i+2][j] == 2 and board[i+3][j] == 2:
        print("win")
      elif board[i][j] == 3 and board[i+1][j] == 3 and board[i+2][j] == 3 and board[i+3][j] == 3:
        print("win")