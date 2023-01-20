slist = []
while True:
    value = input()
    n1, n2 = map(int, value.split())
    if (n1 == 0 and n2 == 0):
        break
    else:
        slist.append(n1 + n2)
for i in slist:
    print(i)
