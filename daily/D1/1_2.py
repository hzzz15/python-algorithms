# K번째 수

N = int(input()) # 테스트 케이스 수

for i in range (N):
    n, s, e, k = map(int,input().split()) # 케이스에 대한 정보
    # n:숫자열 길이 / s,e: s~e까지 / k:k번째 숫자 뽑기
    a = list(map(int, input().split())) # 숫자열 입력 받
    a = a[s-1:e] # s~e번째 숫자 슬라이싱
    a.sort() # 오름차순
    print(a[k-1]) # 정렬한 것 중 k번째 숫자 출력 