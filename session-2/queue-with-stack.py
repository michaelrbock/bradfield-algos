from stack import Stack


class Queue:
  """An implementation of a Queue using two Stacks."""
  def __init__(self):
    # Only one of s1, s2 can have items on it at a time.
    self.s1 = Stack()  # Items only added to s1.
    self.s2 = Stack()  # Items only removed from s2.

  def _swap(self):
    """Swaps all elements from stack with elements to the other."""
    if not self.s1.is_empty():  # Swap to s2.
      while not self.s1.is_empty():
        self.s2.push(self.s1.pop())
    elif not self.s2.is_empty():
      while not self.s2.is_empty():
        self.s1.push(self.s2.pop())

  def is_empty(self):
    return self.s1.is_empty() and self.s2.is_empty()

  def enqueue(self, item):
    """Make sure all items are on s1, then push new item."""
    if not self.s2.is_empty():
      self._swap()
    self.s1.push(item)

  def dequeue(self):
    """Make sure all items are on s2, then pop."""
    if not self.s1.is_empty():
      self._swap()
    return self.s2.pop()

  def size(self):
    return self.s1.size() + self.s2.size()


q = Queue()
assert q.is_empty()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
assert q.size() == 3
assert not q.is_empty()
q.enqueue(8.4)
assert q.dequeue() == 4
assert q.dequeue() == 'dog'
assert q.size() == 2
print('All tests passed!')
