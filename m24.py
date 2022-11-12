sogl = "AO"
glas = "FCD"

with open('C://py_ege//24.txt', 'r') as f:
    chars = f.readlines()[0]
    pairs, max_pairs = 0, 0
    for c in range(0, len(chars), 2):
        if chars[c - 1] in sogl and chars[c] in glas:
            pairs += 1
            max_pairs = pairs if pairs > max_pairs else max_pairs
        else:
            pairs = 0

print(max_pairs)