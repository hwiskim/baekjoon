import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]
results = []

for i in range(N - 7):
    for j in range(M - 7):
        white_start = 0
        black_start = 0
        
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W':
                        white_start += 1
                    if board[a][b] != 'B':
                        black_start += 1
                else:
                    if board[a][b] != 'B':
                        white_start += 1
                    if board[a][b] != 'W':
                        black_start += 1
                        
        results.append(white_start)
        results.append(black_start)

print(min(results))