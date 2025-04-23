# K번째 약수

N, K = map(int, input().split()) # 2개 정수 입력받기 map, split
cnt = 0 # ~번째 작은 수 cnt=0
for i in range (1, N+1):
    if N%i == 0:
        cnt+=1 # N의 약수를 만날때 마다 +1
        if cnt==K: # 누적된 cnt = k 인 경우 i 출력
            print(i)
            break
else:
    print(-1) # 아닌 경우 -1 출력

