x, y, w, h = map(int, input().split())
print(min(h-y, y, x, w-x))