n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
time = 0
total = 0

for i in n_list:
    time+=i
    total+=time

print(total)