li = [9, 3, 5, 7, 1]
print("Before : {}".format(li))
for j in range(1, len(li)):
    key = li[j]
    i = j - 1
    while (i > -1 and li[i] > key):
        li[i+1] = li[i]
        i = i - 1
    li[i+1] = key

print("After : {}".format(li))