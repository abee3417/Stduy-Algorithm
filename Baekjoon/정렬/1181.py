import sys
result = [[] for i in range(51)] #10989와 비슷한 접근방식 : 길이1~50의 문자열들을 담는 리스트를 생성
n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().strip('\n')
    result[len(s)].append(s) #각 길이에 맞는 index로 append
for i in range(51):
    if (len(result[i]) != 0):
        result[i] = sorted(list(set(result[i]))) #중복없애고 재정렬해서
        for j in result[i]: #해당 index의 list를 출력
            print(j)