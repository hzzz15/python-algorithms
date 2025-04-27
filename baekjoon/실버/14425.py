# 문자열 집합

# 1. n,m (기준 단어 n개, 검사할 단어 m개)
# 2. n개 줄은 s에 포함되어 있는 문자열
# 3. m개 줄은 검사해야 하는 문자열 

n,m = map(int, input().split())
s = set()

# 줄마다 하나씩 받음 for문 돌면서 input()
for _ in range(n):
    word = input()
    s.add(word)

cnt = 0

for _ in range(m):
    query = input() # 검사하고 싶은 문자열
    if query in s:
        cnt+=1
print(cnt)