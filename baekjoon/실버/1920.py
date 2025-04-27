# 수 찾기

# 1. 첫번째줄에 자연수 n
# 2. 다음줄에 n개의 정수
# 3. 자연수 m
# 4. m개의 수들 
# 5. m개의 수들이 n개의 정수에 존재하는지 여부 1,0

n=int(input())
n_list = set(map(int, input().split())) # 존재하는지만 확인 = set

m=int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)
