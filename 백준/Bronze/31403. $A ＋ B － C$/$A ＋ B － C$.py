import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
c = sys.stdin.readline().strip()

print(int(a) + int(b) - int(c))

combined_ab = a + b
print(int(combined_ab) - int(c))