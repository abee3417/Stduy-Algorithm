slist = []
T = int(input())
for i in range(T):
    value = input()
    n1, n2 = map(int, value.split())
    slist.append(n1 + n2)
for i in slist:
    print(i)
