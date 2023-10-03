#문자열 뒤집기 : t[::-1], 반대로 가본다는 발상의 전환
def check():
    s = input()
    t = input()
    test, len_s, len_t = t, len(s), len(t)
    for i in range(len_t-1, len_s-1, -1):
        if (test[-1] == 'A'):
            test = test[:i]
        elif (test[-1] == 'B'):
            test = test[:i][::-1]
    if (test == s): return 1
    else: return 0
print(check())