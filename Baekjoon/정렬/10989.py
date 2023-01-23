import sys
n = int(sys.stdin.readline())
arr = [0] * 10001 #숫자는 10000 이하이다.

for i in range(n):
    num = int(sys.stdin.readline())
    arr[num] = arr[num] + 1 #해당 숫자에 해당하는 index값을 1 더해준다. 0->1, 1->2 등

for i in range(10001): #1부터 10000까지의 수 중 0이 아닌, 즉 등장하지 않은 수를 제외한 수를 출력해준다.
    # 숫자마다 index를 부여해 counting해줬으므로 정렬필요없이 당연하게도 1부터 10000까지가 출력된다.
    if (arr[i] != 0):
        for j in range(arr[i]): #중복 수 처리 : 예를 들어 7이 2번나왔다면 i값인 7을 2번 출력할 것이다.
            print(i)
