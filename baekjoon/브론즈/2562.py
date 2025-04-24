# 최댓값
# 1. 자연수 9개
# 2. 이 중 최댓값을 찾고
# 3. 최댓값은 몇번째 수인지

nums = [int(input()) for _ in range(9)] # 9줄에 걸쳐서 숫자가 하나씩 들어옴
max_n = max(nums)

print(max_n)

for i, n in enumerate(nums):
    if n == max_n:
        print(i+1)
        break

# 여러줄 값 하나씩 -> [int(input()) for _ in range(n)]
# 한줄 값 여러개 -> list(map(int, input().split()))