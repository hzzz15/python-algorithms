# 회사에 있는 사람

# 1. 로그에 기록 된 출입 기록 수 n
# 2. 출입 기록이 순서대로 
# 3. 사람 이름 , enter or leave 
# 4. 동명이인 없음 
# 5. enter인 사람만 출력

n = int(input())
person = {} # 딕셔너리로 받기

for _ in range(n):
    name, state = input().split()
    if state == "enter":
        person[name]=True
    else:
        del person[name]

for name in sorted(person.keys(), reverse=True):
    print(name)

# dict : A는 B이다 처럼 추가 정보가 필요할 때
# dict[key] = value, del dict[key]

# set : 이거 있냐 없냐만 보면 될 때
# set.add(value), set.remove(value)