# K번째 큰 수

n, k = map(int, input().split()) 
N_list = list(map(int, input().split())) 
sums = []

# 3중 for문
for i in range (n): 
    for j in range (i+1, n): # i+1시작 --> 같은 카드는 ㄴㄴ
        for m in range (j+1, n): # j+1 시작 --> 같은 카드는 ㄴㄴ
            sums.append(N_list[i] + N_list[j] + N_list[m]) # 3장 더해서 sums리스트에 저장

sums = list(set(sums))
sums.sort(reverse=True) # K번째 큰 수 --> reverse=True

print(sums[k-1]) # 인덱스 위치

# 3장 뽑기 nC3 --> 3중 for문
# 각 조합의 합을 기록 --> 합계산
# 중복제거 --> set
# k번째로 큰 수 --> 정렬 후 인덱스 접근 