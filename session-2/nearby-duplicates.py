"""Given an array of ints and an int k.

Return if there are any duplicates in the array within k indices of each other.

Ex: input = [0, 1, 2, 1, 4, 3], k = 2 -> output: True.
"""

def nearby_duplicates(arr, k):
  arr_map = {}
  for index, elem in enumerate(arr):
    if elem in arr_map:
      if index - arr_map[elem] <= k:
        return True
    arr_map[elem] = index
  return False


def nearby_duplicates2(arr, k):
  arr_set = set()  # Only stores last k items.
  for index, elem in enumerate(arr):
    if elem in arr_set:
      return True
    if index >= k:
      arr_set.remove(arr[index - k])
    arr_set.add(elem)
  return False


for fxn in [nearby_duplicates, nearby_duplicates2]:
  assert fxn([0, 1, 2, 1, 4, 3], 2)
  assert not fxn([0, 1, 2, 5, 4, 3], 2)
  assert not fxn([0, 1, 2, 5, 1, 3], 2)
print('All tests passed!')
