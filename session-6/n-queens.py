'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
N = int(input())


def _is_attacked(board, row, col):
  for cell in board[row]:
    if cell == 1:
      return True
  for i in range(len(board)):
    if board[i][col] == 1:
      return True
  for i in range(len(board)):
    for j in range(len(board[0])):
      if (i + j == row + col or i - j == row - col) and board[i][j] == 1:
        return True


def n_queens(board, n):
  # Base case
  if n == 0:
    return True
  for row in range(len(board)):
    for col in range(len(board[0])):
      if _is_attacked(board, row, col):
        continue
      board[row][col] = 1  # Place queen.
      if n_queens(board, n - 1):
        return True
      board[row][col] = 0  # Backtrack.
  return False


board = [[0 for _ in range(N)] for _ in range(N)]
possible = n_queens(board, N)
if possible:
  print('YES')
  for row in board:
    print(' '.join(map(str, row)))
else:
  print('NO')
