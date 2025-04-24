# 나는야 포켓몬 마스터

# 1. 포켓몬 개수N, 내가 맞춰야 하는 문제 개수M
# 2. 1 ≤ N, M ≤ 100000 --> 시간복잡도 고려 필요
# 3. 포켓몬의 이름은 모두 영어로, 첫글자만 대문자, 일부 포켓몬은 마지막만 대문자
# 4. input 알파벳 <-> output 번호

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

name = {}
num = {}

for i in range(1, n + 1):
    poketmon_name = input().strip()
    name[poketmon_name] = i
    num[i] = poketmon_name # dict에 포켓몬 이름, 숫자 넣기

# input 알파벳 <-> output 번호
for _ in range(m): 
    query = input().strip()
    try:
        print(num[int(query)]) # 숫자면 이름 출력
    except ValueError:
        print(name[query]) # 이름이면 번호 출력

