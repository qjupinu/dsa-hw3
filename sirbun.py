# https://kilonova.ro/problems/556
# O(n)

with open("data/sirbun.in", 'r') as fin:
    n = int(fin.readline())
    v = list(map(int, fin.readline().split()))
freq = {}
total = 0
L = 0
for R in range(n):
    valR = v[R]
    if valR not in freq:
        freq[valR] = 1
    else:
        freq[valR] += 1
    
    while freq[valR] > valR:
        valL = v[L]
        freq[valL] -= 1
        L += 1
    total += R - L + 1

with open("data/sirbun.out", 'w') as fout:
    fout.write(str(total) + '\n')
