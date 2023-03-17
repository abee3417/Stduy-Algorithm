import sys
t = int(input())
for i in range(t):
    # x와 y의 차이를 이용하여 계산한다.
    x, y = map(int, sys.stdin.readline().rstrip().split())
    diff = y - x
    if (diff == 0):
        print(diff)
    else:
        cnt, i = 0, 2
        while (cnt < diff): # cnt를 2의 배수만큼 계속 더해준다.
            cnt += i
            i += 2
        if (diff > cnt-((i-2)//2)): # ex) 10~12, 17~20일 경우
            print(i-2)
        else: # ex) 7~9, 13~16일 경우
            print(i-3)
    '''
    diff기준,
    1일시 1칸, 2일시 2칸 --> 숫자 2개범위 (1~2)
    3~4일시 3칸, 5~6일시 4칸 --> 숫자 4개범위 (3~6)
    7~9일시 5칸, 10~12일시 6칸 --> 숫자 6개범위 (7~12)
    13~16일시 7칸, 17~20일시 8칸 --> 숫자 8개범위 (13~20)
    이런 패턴이 반복되므로 이를 응용하여 계산해준다.
    '''