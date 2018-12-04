"""Merge two sorted lists and return the resulting list."""


def merge_sorted(lst1, lst2):
  index1, index2 = 0, 0
  result = []
  while index1 < len(lst1) and index2 < len(lst2):
    if lst1[index1] <= lst2[index2]:
      result.append(lst1[index1])
      index1 += 1
    else:
      result.append(lst2[index2])
      index2 += 1
  if index1 < len(lst1):
    result += lst1[index1:]
  elif index2 < len(lst2):
    result += lst2[index2:]
  return result


assert merge_sorted([1, 1, 2, 3], [1, 3, 5]) == [1, 1, 1, 2, 3, 3, 5]
assert merge_sorted([], [1, 3, 5]) == [1, 3, 5]
assert merge_sorted([1, 3, 5], []) == [1, 3, 5]
print('All tests passed!')
