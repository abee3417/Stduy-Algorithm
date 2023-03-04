import sys
t = int(input())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().rstrip().split()) # 각각 층수, 방수, 손님순서
    floor = n % h
    room = n // h
    if (floor == 0):
        floor = h
    else:
        room += 1
    print(100 * floor + room)

'''
<알고리즘 풀이>
import sys
t = int(input())
for i in range(t):
    floor, room = 0, 1
    h, w, n = map(int, sys.stdin.readline().rstrip().split()) # 각각 층수, 방수, 손님순서
    for j in range(n):
        if (floor < h):
            floor += 1
        else:
            floor = 1
            room += 1
    if (room < 10):
        print(str(floor) + '0' + str(room))
    else:
        print(str(floor) + str(room))
'''
