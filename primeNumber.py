import math

n = int(input())
ans = 0
xd = []
for i in range(n + 1):
    xd.append(0)
for i in range(2, int(math.sqrt(n) + 1)):
    if xd[i] == 0:
        j = i + i
        while j <= n:
            xd[j] = 1
            j += i

for i in range(1, n + 1):
    if xd[i] == 0:
        ans += i

print(ans)
