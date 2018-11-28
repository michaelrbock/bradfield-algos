def shift(arr, k):
  # Mod by length of arr to account for multiple rotational shifts.
  k = k % len(arr)
  if k <= 0 or not arr:
    return arr
  start, index = 0, 0  # start and current index.
  next_num = arr[index]
  for iteration in range(len(arr)):
    destination = index - (len(arr) - k)
    next_num, arr[destination] = arr[destination], next_num
    # Convert possibly negative indexes to positive for next itertion.
    index = destination if destination >= 0 else len(arr) + destination
    if index == start:  # Make sure we avoid loops.
      index += 1
      start = index
      next_num = arr[index]
  return arr


assert shift([1], 0) == [1]
assert shift([1], 1) == [1]
assert shift([1, 2], 1) == [2, 1]
assert shift([1, 2, 3], 1) == [3, 1, 2]
assert shift([1, 2, 3], 2) == [2, 3, 1]
assert shift([1, 2, 3], 3) == [1, 2, 3]
assert shift([1, 2, 3, 4], 3) == [2, 3, 4, 1]
assert shift([1, 2, 3, 4], 5) == [4, 1, 2, 3]
assert shift([1, 2, 3, 4, 5, 6], 3) == [4, 5, 6, 1, 2, 3]
assert shift([1, 2, 3, 4, 5, 6], 2) == [5, 6, 1, 2, 3, 4]
# # Array does not need to be sorted.
assert shift(['c', 'd', 'a'], 7) == ['a', 'c', 'd']
print('All tests passed!')
