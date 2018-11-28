def shift(arr, k):
  if k <= 0:
    return arr
  # Mod by length of arr to account for multiple rotational shifts.
  k = k % len(arr)
  index = 0  # current index.
  next_num = arr[index]
  for _ in range(len(arr)):
    destination = index - (len(arr) - k)
    next_num, arr[destination] = arr[destination], next_num
    # Convert possibly negative indexes to positive for next itertion.
    index = destination if destination >= 0 else len(arr) + destination
  return arr


assert(shift([1], 1)) == [1]
assert(shift([1, 2], 1)) == [2, 1]
assert(shift([1, 2, 3], 1)) == [3, 1, 2]
assert(shift([1, 2, 3], 2)) == [2, 3, 1]
assert(shift([1, 2, 3], 3)) == [1, 2, 3]
assert(shift([1, 2, 3, 4], 3)) == [2, 3, 4, 1]
assert(shift([1, 2, 3, 4], 5)) == [4, 1, 2, 3]
# Array does not need to be sorted.
assert(shift(['c', 'd', 'a'], 7)) == ['a', 'c', 'd']
print('All tests passed!')
