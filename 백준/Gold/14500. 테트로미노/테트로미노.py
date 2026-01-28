import sys

tetrominos = [
    #작대기
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    #직사각형
    [(0,0), (0,1), (1,0), (1,1)],
    
    #ㅗ 자
    [(0,0), (0,1), (0,2), (1,1)],
    [(0,0), (1,0), (2,0), (1,1)],
    [(1,0), (1,1), (1,2), (0,1)],
    [(0,0), (1,0), (2,0), (1,-1)],
    
    #L자 정의
    [(0,0), (1,0), (2,0), (2,1)],
    [(0,0), (0,1), (0,2), (1,0)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,2), (1,0), (1,1), (1,2)],
    [(0,0), (1,0), (2,0), (2,-1)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (0,1), (0,2), (1,2)],
    
    #z 정의
    [(0,0), (0,1), (1,1), (1,2)],
    [(0,1), (1,0), (1,1), (2,0)],
    [(0,1), (0,2), (1,0), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
]

def inRange(x,y):
    if x in range(n) and y in range(m):
        return True
    else:
        return False



n, m = map(int, sys.stdin.readline().split())

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
            
max_sum = 0
for i in range(n):
    for j in range(m):
        for tetro in tetrominos:
            temp = 0
            valid = True
            for dx, dy in tetro:
                ni, nj = i + dx, j + dy
                if inRange(ni, nj):
                    temp += grid[ni][nj]
                else:
                    valid = False
                    break
            if valid:
                max_sum = max(max_sum, temp)
print(max_sum)