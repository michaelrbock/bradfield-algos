def spiral(m, n):
  """Return spiral matrix of m row and n cols."""
  matrix = [[0] * n for _ in range(m)]
  direction = 'R'
  row, col = 0, 0
  for num in range(1, m * n + 1):
    matrix[row][col] = num
    if direction == 'R':
      col += 1
      if col >= len(matrix[0]) or matrix[row][col] != 0:
        direction = 'D'
        col -= 1
        row += 1
    elif direction == 'D':
      row += 1
      if row >= len(matrix) or matrix[row][col] != 0:
        direction = 'L'
        row -= 1
        col -= 1
    elif direction == 'L':
      col -= 1
      if col < 0 or matrix[row][col] != 0:
        direction = 'U'
        col += 1
        row -= 1
    else:  # direction == 'U'
      row -= 1
      if row < 0 or matrix[row][col] != 0:
        direction = 'R'
        row += 1
        col += 1
  return matrix


print(spiral(1, 1))
print(spiral(2, 2))
print(spiral(3, 3))
print(spiral(3, 4))
