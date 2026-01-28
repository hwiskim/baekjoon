import heapq
import sys

def solve():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    
    if n >= k:
        print(n - k)
        return

    max_pos = 100001
    dist = [float('inf')] * max_pos
    dist[n] = 0
    pq = [(0, n)]

    while pq:
        d, curr = heapq.heappop(pq)

        if dist[curr] < d:
            continue
        
        if curr == k:
            print(d)
            break

        for next_pos, weight in [(curr * 2, 0), (curr - 1, 1), (curr + 1, 1)]:
            if 0 <= next_pos < max_pos:
                if dist[next_pos] > d + weight:
                    dist[next_pos] = d + weight
                    heapq.heappush(pq, (dist[next_pos], next_pos))

solve()