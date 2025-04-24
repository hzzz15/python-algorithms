n = int(input())
data = []

for idx in range(n):
    age, name = input().split()
    data.append((int(age), idx, name))  

data.sort(key=lambda x: (x[0], x[1]))

for d in data:
    print(d[0], d[2])
