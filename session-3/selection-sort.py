def _get_min_index(arr, start):
  """Get the index of the min element after the start index."""
  min_index = start
  for i in range(start + 1, len(arr)):
    if arr[i] < arr[min_index]:
      min_index = i
  return min_index


def selection_sort(arr):
  """In-place selection sort of arr."""
  for i in range(len(arr)):
    min_index = _get_min_index(arr, i)
    if i != min_index:
      arr[i], arr[min_index] = arr[min_index], arr[i]


test_cases = [
  ([], []),
  ([1], [1]),
  ([2, 1], [1, 2]),
  ([3, 2, 1], [1, 2, 3])
]

for case, expected in test_cases:
  selection_sort(case)
  assert case == expected
print('All tests passed!')
