import sys
sys.setrecursionlimit(100000)

def pre_trav(n):
    if (n == -1): return
    print(chr(n+65), end="")
    pre_trav(tree[n][0])
    pre_trav(tree[n][1])
    return

def in_trav(n):
    if (n == -1): return
    in_trav(tree[n][0])
    print(chr(n+65), end="")
    in_trav(tree[n][1])
    return

def post_trav(n):
    if (n == -1): return
    post_trav(tree[n][0])
    post_trav(tree[n][1])
    print(chr(n+65), end="")
    return

n = int(input())
tree = [[-1, -1] for _ in range(n)]
visit = [0 for _ in range(n)]
for _ in range(n):
    n1, n2, n3 = map(str, input().split())
    if (n2 != '.'):
        tree[ord(n1)-65][0] = ord(n2)-65
    if (n3 != '.'):
        tree[ord(n1)-65][1] = ord(n3)-65
pre_trav(0)
print()
in_trav(0)
print()
post_trav(0)