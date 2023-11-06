'''
측정구간이 [1, 10]에서 무게5의 추가 더해진다면, 구간을 [1+5, 10+5]로 바꿀 수 있다.
만약 바뀐 구간의 idx0(6)이 원래 구간의 idx1+1(10)보다 작거나 같다면 범위가 겹친다는 뜻이므로
측정구간을 [1, 10+5]로 바꿀 수 있다.
이렇게 갱신하다가 조건이 만족하지 않을 때 원래 구간의 idx+1을 출력하면 된다.
기존 구간 : [0, 누적합[i-1]], 바뀐 구간 : [무게[i], 누적합[i]], 무게[i] <= 누적합[i-1]+1 만족 시 범위갱신
'''
n = int(input())
w = list(map(int, input().split()))
w.append(0)
w.sort()
w_sum = [0]
w_len = len(w)
flag = False
for i in range(1, w_len): #위 원리를 이용한 누적합배열 사용
    w_sum.append(w_sum[i-1] + w[i])
for i in range(1, w_len):
    if (w[i] > w_sum[i-1] + 1): #조건 만족하지 못할 시 break
        flag = True
        print(w_sum[i-1] + 1)
        break
if (flag == False):
    print(w_sum[w_len-1] + 1)