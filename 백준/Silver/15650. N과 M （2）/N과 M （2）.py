def dfs(start, arr):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(start, n + 1):
        dfs(i + 1, arr + [i])


n, m = map(int, input().split())

dfs(1, [])