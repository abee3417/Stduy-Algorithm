#참고한 글 : 나무위키 "피보나치 수열" 8.1
import sys
sys.setrecursionlimit(10**6)
DIV = 1000000007
def divide(n):
    if (n == 1):
        return 1, 1, 0 #F_2, F_1, F_0
    else:
        f1, f, f_1 = divide(n//2)
        conq_f1, conq_f, conq_f_1 = (f1**2+f**2)%DIV, (f1*f+f*f_1)%DIV, (f**2+f_1**2)%DIV
        if (n%2 == 0):
            return conq_f1, conq_f, conq_f_1
        else:
            return (conq_f1+conq_f)%DIV, (conq_f1)%DIV, (conq_f)%DIV

n = int(input())
tmp1, ans, tmp2 = divide(n)
print(ans % DIV)