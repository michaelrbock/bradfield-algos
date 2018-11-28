"""Staircase robot problem. How many ways can robot jump 1 or 2 steps to n."""

def stairs(n):
  if n <= 2:
    return n
  prev = 0
  curr = 1
  for _ in range(n):
    curr, prev = curr + prev, curr
  return curr


assert stairs(1) == 1
assert stairs(2) == 2
assert stairs(3) == 3
assert stairs(4) == 5
assert stairs(5) == 8
assert stairs(6) == 13
print('All tests passed!')
