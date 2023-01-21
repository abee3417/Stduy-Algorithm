nstr = 1
for i in range(3):
    nstr *= int(input())
nstr = str(nstr)
for i in range(0,10):
    print(nstr.count(str(i)))