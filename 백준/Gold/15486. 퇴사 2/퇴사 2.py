import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
T = []

for _ in range(N) :
    T.append(list(map(int, input().split())))

DP = [0 for _ in range(N + 1)]

for i in range(1, N + 1) :
    DP[i] = max(DP[i - 1], DP[i])
    if i + T[i - 1][0] <= N + 1 :
        DP[i + T[i - 1][0] - 1] = max(DP[i + T[i - 1][0] - 1], DP[i - 1] + T[i - 1][1])

print(DP[-1])