"""Given two absolute paths, return if they point to the same file. E.g.:

'/foo/bar/./baz/../bat', '/foo/bar/bat' --> yes.
"""

def _normalize(path):
  parts = path.split('/')[1:]
  normalized = []
  for part in parts:
    if part == '.':
      pass
    elif part == '..':
      normalized.pop()
    else:
      normalized.append(part)
  return normalized


def same_path(path1, path2):
  return _normalize(path1) == _normalize(path2)


assert same_path('/foo/bar/./baz/../bat', '/foo/bar/bat')
print('All tests passed!')