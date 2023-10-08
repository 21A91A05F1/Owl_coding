N = int(input())
Cur = int(input())
pos = list(map(int, input().split()))
time = list(map(int, input().split()))
min_time=9999999999999
distance=dist_time=0
for i in range(N):
    distance=abs(Cur-pos[i])
    dist_time=distance*time[i]
    min_time=min(min_time,dist_time)
print(min_time)
