import sys

n = int(sys.stdin.readline())
sizes = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())

total_t_bundles = 0
for s in sizes:
    if s > 0:
        total_t_bundles += (s + t - 1) // t

print(total_t_bundles)
print(n // p, n % p)