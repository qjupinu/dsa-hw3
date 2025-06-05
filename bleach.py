# https://infoarena.ro/problema/bleach
# O(n log n)

with open("data/bleach.in", "r") as f:
    n, k = map(int, f.readline().split())
    power = list(map(int, f.readline().split()))
power.sort()
current_power = 0
init_power = 0
for p in power:
    if current_power < p:
        delta = p - current_power
        init_power += delta
        current_power += delta
    current_power += p
# init_power is now the result

with open("data/bleach.out", "w") as f:
    f.write(f"{init_power}\n")
