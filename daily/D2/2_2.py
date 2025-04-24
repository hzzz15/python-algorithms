# 정다면체

# 1. 두개의 정n,m 면체
# 2. 두개의 주사위를 던져서 나올수 있는 합 -> max
# 3. 합중 가장 확률이 높은 숫자를 출력 
# 4. 정답이 여러 개 인 경우 오름차순으로 출력 --> sort

n, m = map(int, input().split()) 
cnt = [0] * (n+m+1) # 인덱스 땜에 +1

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]+=1 # 같은 합의 경우인 경우 +1
max_count = max(cnt)

for i in range(2, n+m+1):
    if cnt[i] == max_count:
        print(i, end=' ')
