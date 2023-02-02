s = input()
judg = 1
for i in range(len(s)//2):
    if (s[i] != s[-(i+1)]):
        judg = 0
print(judg)