while True:
    try:
        value = input()
        n1, n2 = map(int, value.split())
        print(n1 + n2)
    except:
        break
