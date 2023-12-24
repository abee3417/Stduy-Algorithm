x, y = set(), set()
for _ in range(3):
    X, Y = map(int, input().split())
    if (X in x): x.remove(X)
    else: x.add(X)
    if (Y in y): y.remove(Y)
    else: y.add(Y)
print(x.pop(), y.pop())