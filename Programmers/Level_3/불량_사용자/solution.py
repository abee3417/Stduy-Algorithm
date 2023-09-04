# 응모자 배열 user_id, 불량 사용자 목록 banned_id
# 아이디 목록은 몇가지 경우의 수가 존재?

import itertools

def solution(user_id, banned_id):
    result = []
    answer = 0
    flag = 0
    ban_length = len(banned_id)
    data = list(itertools.permutations(user_id, ban_length))
    for i in data:  
        for j in range(len(i)):
            std = len(i[j])
            if (std == len(banned_id[j])):
                for k in range(std):
                    if (i[j][k] != banned_id[j][k] and banned_id[j][k] != '*'):
                        break
                    if (k == std - 1):
                        flag += 1
        if (flag == ban_length):
            tmp = set(list(i))
            if (tmp not in result):
                result.append(tmp)
        flag = 0
    answer = len(result)
    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
