def insertion_sort(arr):
  """In-place insertion sort on arr."""
  for j in range(len(arr)):
    for i in range(j, 0, -1):
      if arr[i] >= arr[i-1]:
        continue
      arr[i], arr[i-1] = arr[i-1], arr[i]


test_cases = [
  ([], []),
  ([1], [1]),
  ([2, 1], [1, 2]),
  ([3, 2, 1], [1, 2, 3])
]

for case, expected in test_cases:
  insertion_sort(case)
  assert case == expected
print('All tests passed!')
