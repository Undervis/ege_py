for a in range(1, 500):
    is_true = True
    for x in range(1, 500):
        f = (not x % 2 == 0 or x % 3 != 0) or (x + a >= 100)
        if not f:
            is_true = False
            break
    if is_true:
        print(a)
        break
