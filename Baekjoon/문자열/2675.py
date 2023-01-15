T = int(input())
slist = []
S2 = ''
for i in range(T):
    value = input()
    R = int(value.split()[0])
    S1 = value.split()[1]
    for j in range(len(S1)):
        S2 += S1[j] * R
    slist.append(S2)
    S2 = ''
for i in slist:
    print(i)
