# https://infoarena.ro/problema/pikachu
# O (n k log k)

with open("data/pikachu.in", "r") as fin:
    n, k = map(int, fin.readline().split())
    heights = list(map(int, fin.readline().split()))
min_time = 1e9
for i in range(n - k + 1):
    cost = heights[i : i + k]
    sorted_cost = sorted(cost)
    median = sorted_cost[k // 2]
    time = 0
    # time needed to get all heights to median value
    for h in cost:
        time += abs(h - median)
    if time < min_time:
        min_time = time
with open("data/pikachu.out", "w") as fout:
    fout.write(f"{min_time}\n")
