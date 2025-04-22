n = int(input())

for _ in range(n):
    a = input().strip()
    cnt = 0 
    sum = 0
    for i in range(len(a)):
        if a[i] == "O":
            cnt+=1
            sum+=cnt
        else:
            cnt = 0
    print(sum)