from stack import Stack


def reverse(lst):
  """Returns a reversed copy of input using a stack."""
  stack = Stack()
  for elem in lst:
    stack.push(elem)
  result = []
  while not stack.is_empty():
    result.append(stack.pop())
  return result


assert reverse([]) == []
assert reverse([1]) == [1]
assert reverse([1, 2, 3]) == [3, 2, 1]
assert reverse(['a', 'a', 'b']) == ['b', 'a', 'a']
print('All tests passed!')