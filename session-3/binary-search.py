def binary_search(lst, target):
  """Returns index of target in a sorted lst, or -1 if target not present."""
  start, end = 0, len(lst) - 1
  while start <= end:
    mid = (start + end) // 2
    if lst[mid] == target:
      return mid
    elif lst[mid] < target:
      start = mid + 1
    else:  # lst[mid] > target
      end = mid - 1
  return -1


assert binary_search([], 0) == -1
assert binary_search([0], 0) == 0
assert binary_search([0, 2, 4], 2) == 1
assert binary_search([0, 2, 4, 4], 4) == 2
assert binary_search([0, 2, 4, 4], 5) == -1
assert binary_search([0, 0, 4], -1) == -1
print('All tests passed!')
