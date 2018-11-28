ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def panagram1(string):
  """T: O(n), S: O(n)"""
  string_set = set(string)
  return all(letter in string_set for letter in ALPHABET)


def panagram2(string):
  """T: O(26 * n), S: O(1)"""
  for letter in ALPHABET:
    if letter not in string:
      return False
  return True


def panagram3(string):
  """T: O(nlogn), S: O(n)"""
  sorted_string = ''.join(sorted(string)).strip()
  string_index = 0
  alphabet_index = 0
  while string_index < len(sorted_string) and alphabet_index < len(ALPHABET):
    if sorted_string[string_index] == ALPHABET[alphabet_index]:
      string_index += 1
    else:
      alphabet_index += 1
      if sorted_string[string_index] != ALPHABET[alphabet_index]:
        return False
  return string_index == len(
      sorted_string) and alphabet_index == len(ALPHABET) - 1


assert panagram1('the quick brown fox jumps over the lazy dog')
assert panagram1('the quick brown fox jumps over the lazy do') == False
assert panagram2('the quick brown fox jumps over the lazy dog')
assert panagram2('the quick brown fox jumps over the lazy do') == False
assert panagram3('the quick brown fox jumps over the lazy dog')
assert panagram3('the quick brown fox jumps over the lazy do') == False
print('All tests passed!')
