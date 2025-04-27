# 대칭 차집합

# 1. 집합 A의 원소의 개수 B의 원소의 개수
# 2. 집한 A의 모든 원소
# 3. 집합 B의 모든 원소
# 4. print 원소들의 차집합 원소 개수 

a, b = map(int, input().split())
a_list = set(map(int, input().split()))
b_list = set(map(int, input().split()))

result = a_list ^ b_list # 대칭 차집합

print(len(result))