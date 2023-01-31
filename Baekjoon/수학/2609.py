def gcd(n1, n2):
    if (n2 == 0):
        return n1
    return gcd(n2, n1 % n2)

a, b = map(int, input().split())
_gcd = gcd(a, b)
_lcm = a * b // _gcd
print(_gcd, _lcm)