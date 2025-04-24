# 평균

# 1. 점수중 최댓값 선택 -> M
# 2. 모든 점수를 M*100으로 수정

n=int(input())
score = list(map(int, input().split()))
M = max(score)

for i, s in enumerate(score):
    score[i] = s/M*100

score = sum(score) / n
print(score)