import sys
n = int(input())
li1 = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
li2 = list(map(int, sys.stdin.readline().rstrip().split()))
li1.sort()
for i in li2:
    flag = False
    left = 0
    right = len(li1) - 1
    while (left <= right):
        mid = (left + right) // 2
        if (i < li1[mid]):
            right = mid - 1
        elif (i > li1[mid]):
            left = mid + 1
        else:
            flag = True
            break
    if (flag == True):
        print("1")
    else:
        print("0")