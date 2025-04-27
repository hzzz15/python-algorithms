# 좌표 정렬하기

# 1. 점 N개 (2차원)
# 2. x좌표가 증가하는 순
# 3. x좌표가 같으면 y좌표가 증가

n = int(input())
data = []

for _ in range(n):
    x, y = map(int, input().split())
    data.append([x,y])

data.sort(key=lambda x: (x[0], x[1]))

for i in data:
    print(i[0], i[1])