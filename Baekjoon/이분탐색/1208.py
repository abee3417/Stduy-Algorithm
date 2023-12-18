#Meet In The Middle(MTIM) 알고리즘 문제
'''
큰 문제를 2개로 나눠서 푸는 방법
분할정복과 다르게 재귀적으로 base case까지 나누는게 아닌, 절반으로 나누어 처리해서 연산 횟수를 감소
이 문제에서는, 2개로 나누어 중복조합의 모든 합을 구해 놓고,
투포인터를 이용해서 두 합이 S와 같은지를 확인할 것이다.
이때 포인터 한개는 전반부 리스트의 0번째부터, 나머지 한개는 후반부 리스트의 -1번째부터 탐색한다.
그래서 중간에서 만나기 전까지 탐색한다. 
'''
import sys
from itertools import combinations
input = sys.stdin.readline
N, S = map(int, input().split())
li = sorted(list(map(int, input().split())))
li1, li2 = li[:N//2], li[N//2:]
sum_li1, sum_li2 = [0], [0] #좌우 sum배열에 이미 S가 있는 경우 S+0도 고려해야 하므로 0을 넣어준다. 대신 ans를 출력할 때 S가 0일 때는 1을 빼준다.
ans = 0
for i in range(1, len(li1)+1):
    tmp = combinations(li1, i) #li1에서 i개뽑은 모든 부분집합
    for j in tmp:
        sum_li1.append(sum(j)) #그 부분집합들을 합한 모든 경우를 append
for i in range(1, len(li2)+1):
    tmp = combinations(li2, i) #li1에서 i개뽑은 모든 부분집합
    for j in tmp:
        sum_li2.append(sum(j)) #그 부분집합들을 합한 모든 경우를 append
sum_li1.sort()
sum_li2.sort()
left, right = 0, len(sum_li2)-1
while (left < len(sum_li1) and 0 <= right):
    val = sum_li1[left] + sum_li2[right]
    if (val == S):
        tmp_left, tmp_right = left, right
        left, right = left+1, right-1 #우선 기본적으로 두 포인터 모두 이동해주고,
        left_ans, right_ans = 1, 1
        #합 리스트 안에 중복값이 있을 수 있으므로 이들도 고려해준다. (ex. S=10이고 [0, 3, 3, 3, 3, 4], [7, 7, 7, 17]일 때 답은 12가 나와야 한다.)
        while (left < len(sum_li1) and sum_li1[tmp_left] == sum_li1[left]):
            left += 1
            left_ans += 1
        while (0 <= right and sum_li2[tmp_right] == sum_li2[right]):
            right -= 1
            right_ans += 1
        ans += (left_ans * right_ans) #ans 정산, 왼쪽에서 나온 정답값 수 * 오른쪽에서 나온 정답값 수
    elif (val < S): #S보다 작으면 왼쪽 포인터를 우측 이동
        left += 1
    else: #S보다 크면 오른쪽 포인터를 좌측 이동
        right -= 1
print(ans if (S != 0) else ans-1)