import sys

# N을 입력받습니다 (1 ≤ N ≤ 100)
n = int(sys.stdin.readline())

# 1부터 n까지 반복
for i in range(1, n + 1):
    # (n-i)개의 공백과 i개의 별을 합쳐서 출력
    print(" " * (n - i) + "*" * i)