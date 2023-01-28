s = sorted(list(input()))
alp = {} # 딕셔너리를 사용, key : 알파벳, 값 : 갯수
for i in range(len(s)): # 딕셔너리 구축
    if (s[i] in alp.keys()):
        alp[s[i]] += 1
    else:
        alp[s[i]] = 1
k_list = list(alp.keys())
v_list = list(alp.values())
result = ['' for i in range(len(s))]
# 팰린드롬을 만들기 위한 변수들
odd_cnt = 0
odd_alp = ''
even_cnt = 0
start = 0
end = len(s) - 1
# 짝홀 갯수 판별
for i in range(len(v_list)):
    if (v_list[i] % 2 == 0):
        even_cnt += 1
    else:
        odd_cnt += 1
        odd_alp = k_list[i]
# 조건1. 모든 알파벳 개수가 짝수일 때
if (odd_cnt == 0):
    for i in k_list:
        if (start > end):
            break
        for j in range(alp[i] // 2):
            result[start], result[end] = i, i
            start += 1
            end -= 1
    print(''.join(result))
# 조건2. 1가지 알파벳 개수가 홀수이고 문자열 길이가 홀수일 때
elif (odd_cnt == 1 and len(s) % 2 == 1):
    #홀수일 시 값 하나를 중간값으로 두고 하나 빼준다.
    result[end//2] = odd_alp 
    alp[odd_alp] -= 1
    for i in k_list:
        if (start > end):
            break
        for j in range(alp[i] // 2):
            result[start], result[end] = i, i
            start += 1
            end -= 1
    print(''.join(result))
# 조건1, 조건2 불만족시 팰린드롬 X
else:
    print("I'm Sorry Hansoo")