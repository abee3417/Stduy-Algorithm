n = input()
base, ans = int(n), 0
while True:
    ans += 1
    if (int(n) < 10):
        tmp = n + '0'
        new_n = str(int(tmp[0]) + int(tmp[1]))
    else:
        new_n = str(int(n[0]) + int(n[1]))
    n = n[-1] + new_n[-1]
    if (int(n) == base):
        print(ans)
        break