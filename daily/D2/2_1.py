# 대표값

# 1. n명 학생의 수학점수
# 2. 학생들의 평균 (소수 첫째자리 반올림)
# 3. 학생들중 평균에 가장 가까운 학생이 누구인지
# > 평균과 가장 작은순, 점수가 높은순, 번호 빠른 순
# 4. 평균과 가까운 학생이 여러명 --> 점수가 높은 학생이 먼저
# 5. 높은 학생이 여러 명인 경우 학생번호가 빠른 학생이 답 -->index

n = int(input())
n_list = list(map(int, input().split())) 
n_avg = round(sum(n_list) / n)

min_diff = float('inf') # 무한대 값 / 처음에 어떤 값이 오든 무조건 작다고 판단되게 하기 위해서 사용 / 누구든 처음에 무조건 min_diff보다 작음 -> 조건문 안으로 들어감 -> 최솟값 갱신 가능
result_score = 0
result_idx = 0

for idx, score in enumerate(n_list): # 인덱스 값을 동시에 꺼내기 
    diff = abs(score - n_avg) # 평균과 차이나는지 절댓값으로 저장

    if diff < min_diff: #새로운 최소 차이 발견 -> 갱신
        min_diff = diff
        result_score = score
        result_idx = idx
    elif diff == min_diff:
        if score > result_score: # 같은 차이면 score 높은 학생 선택
            result_score = score
            result_idx = idx
        elif score == result_score: # 점수도 같으면 idx 빠른 학생 선택
            if idx < result_idx:
                result_idx = idx

print(n_avg, result_idx+1)

        


