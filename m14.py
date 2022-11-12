import string

n = 15
alph = '0123456789' + string.ascii_lowercase[:n-10]

for x in alph:
    exp = int(f'123{x}5', n) + int(f'1{x}233', n)
    if exp % 14 == 0:
        print(exp // 14)
        break
