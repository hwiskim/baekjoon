n, m = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()

def dfs(start, arr):
    if len(arr) == m:
        print(*arr)
        return
    for i in num_list:
        if i in arr:
            continue
        dfs(i, arr + [i])


dfs(-1, [])