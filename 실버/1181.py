n = int(input())
data = []
for i in range(n):
    data.append(input())
set_data = set(data)
data = list((set_data))

data.sort()
data.sort(key=len)

for i in data:
    print(i)