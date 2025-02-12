import sys
sys.stdin = open("input.txt", "r")

def combination(arr, r):
    acc = [] #누적 결과값을 넣을 배열
    if r == 1: #선택할 요소의 수가 1인 경우
        return [[i] for i in arr]
    #배열에 대해 반복
    for i in range(len(arr)):
        elem = arr[i] #현재 요소를 선택
        for rest in combination(arr[i+1:],r-1):
            acc.append([elem]+rest)
    return acc

T = int(input())

for test_case in range(1,T+1):
    #N 사람ㅅ수, B : 선반의 수
    N, B = map(int,input().split())
    arr = list(map(int, input().split()))
    #최종 결과값 -> 우리는 B를 넘는 값중 제일 낮은 값
    #아래는 너무 큰 값
    # result = float('inf') #충분히 큰 값
    result = 10000 * 20 + 1
    #완점 탐색
    for r in range(1, N+1): #1부터 N명까지 선택
        #전체 배열에서 arr에서 r명 선택한 조합
        for comb in combination(arr,r):
            total_height = sum(comb) #조합의 총합
            if total_height >= B: #선반보다는 높아야함
                #그렇게 얻은 B보다 큰 값중, 제일 작은 값

                result = min(total_height, result)
    print(f'#{test_case} {result}')