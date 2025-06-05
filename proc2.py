# https://www.infoarena.ro/problema/proc2
# O (m log n)

import heapq
with open("data/proc2.in", 'r') as fin:
    n, m = map(int, fin.readline().split())
    tasks = [tuple(map(int, fin.readline().split())) for _ in range(m)]

""" 2 heaps for available and busy processors, where
# procs_busy is based on processor S_i (when it becomes available) and its index"""
procs_available = list(range(1, n + 1))
procs_busy = []
heapq.heapify(procs_available)
output = []
for S_i, D_i in tasks:
    # free available processors
    while procs_busy and procs_busy[0][0] <= S_i:
        old_si, id = heapq.heappop(procs_busy)
        heapq.heappush(procs_available, id)
    
    # allocate the processor with the smallest id, and mark it as busy until S_i + D_i
    id = heapq.heappop(procs_available)
    output.append(id)
    heapq.heappush(procs_busy, (S_i + D_i, id))

with open("data/proc2.out", 'w') as fout:
    for proc in output:
        fout.write(f"{proc}\n")

