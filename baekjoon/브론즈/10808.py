s = input()
lst = [0] * 26

for i in range(26):  
    ch = chr(i + ord('a')) 
    lst[i] = s.count(ch)

print(*lst)
