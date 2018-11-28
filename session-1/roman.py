VALUES = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000,
}

def roman(digits):
  total = 0
  i = 0
  while i < len(digits):
    if i == len(digits) - 1 or VALUES[digits[i]] >= VALUES[digits[i+1]]:
      total += VALUES[digits[i]]
      i += 1
    else:
      total += VALUES[digits[i+1]] - VALUES[digits[i]]
      i += 2
  return total


assert roman('I') == 1
assert roman('II') == 2
assert roman('IV') == 4
assert roman('V') == 5
assert roman('VIII') == 8
assert roman('IX') == 9
assert roman('XV') == 15
assert roman('XX') == 20

print('All tests passed!')