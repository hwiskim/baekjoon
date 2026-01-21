numbers = list(map(int, input().split()))

total_sum = 0

for num in numbers:
    total_sum += num ** 2

print(total_sum % 10)