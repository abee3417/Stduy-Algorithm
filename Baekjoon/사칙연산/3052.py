n1 = []
for i in range(10):
    n1.append(int(input()) % 42)
n1 = list(set(n1))
print(len(n1))