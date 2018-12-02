from stack import Stack


class Queue:
  """An implementation of a Queue using two Stacks."""
  def __init__(self):
    self.s1 = Stack()  # Items only added to s1.
    self.s2 = Stack()  # Items only removed from s2.

  def is_empty(self):
    return self.s1.is_empty() and self.s2.is_empty()

  def enqueue(self, item):
    """Time: O(1)"""
    self.s1.push(item)

  def dequeue(self):
    """If s2 is empty, reverse items from s1 onto s2 and pop. Time: O(n)."""
    if self.s2.is_empty():
      while not self.s1.is_empty():
        self.s2.push(self.s1.pop())
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
