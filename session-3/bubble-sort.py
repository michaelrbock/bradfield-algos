def bubble_sort(arr):
  """In-place bubble sort on arr."""
  for j in range(len(arr) - 1, -1, -1):
    for i in range(j):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]


test_cases = [
  ([], []),
  ([1], [1]),
  ([2, 1], [1, 2]),
  ([3, 2, 1], [1, 2, 3])
]

for case, expected in test_cases:
  bubble_sort(case)
  assert case == expected
print('All tests passed!')
