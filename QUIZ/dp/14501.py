N = int(input())
t = []
p = []
dp = []
for _ in range(N):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)
dp = p
dp.append(0)

for i in range(N-1,-1,-1):
    if t[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],p[i]+dp[i + t[i]])

print(dp[0])
