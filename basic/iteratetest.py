d = {'a': 1, 'b': 2, 'c': 3}
for value in d:
    print(value)

for value in d.values():
    print(value)

for c in 'ABC':
    print(c)

from collections.abc import Iterable

b = isinstance('ABC', Iterable)
print(b)

for i, v in enumerate(['A', 'B', 'C']):
    print(i)
    print(v)

for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)
