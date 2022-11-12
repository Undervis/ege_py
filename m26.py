with open('C://py_ege//26.txt', 'r') as f:
    n = int(f.readline())
    length = [int(i) for i in f]
    length.sort(reverse=True)

    count = 1
    max_length = length[0]
    for i in range(1, len(length)):
        if max_length - length[i] >= 3:
            count += 1
            max_length = length[i]

print(count, max_length)