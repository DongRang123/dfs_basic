import sys
from wsgiref.util import request_uri

sys.stdin = open("input.txt", "r")
#idx : 조사 대상의 index
#count : 조사한 대상의 수
#total : 그 대상들의 키의 합
def dfs(idx,count,total ):
    global result
    if total>=B:
        result = min(total,result)
        return

    if idx ==N or count == N:
        return
    #현재 index 번째 사람을 조사 대상에 추가하고 다음 사람 조사
    #다음 사람 조사를 위해 index 1증가
    #현재 사람을 선택했으니 count 1증가
    #현재 사람의 키 만큼을 total에 추가

    dfs(idx+1, count+1, total + arr[idx])
    #현재 번재 사람을 total에 추가히지 않고 ,넘어감
    #따라서 count 1증가 ㄴㄴ
    #따라서 total도 증가하지 않음
    #단, 다음 사람을 조사하러 갈것이기 때문에 idx만 1증가
    dfs(idx+1,count,total)


T = int(input())
for test_case in range(1,T+1):
    #N 사람수, B : 선반의 수
    N, B = map(int,input().split())
    arr = list(map(int, input().split()))

    result = 10000 * 20 + 1

    dfs(0,0,0)


    print(f'#{test_case} {result-B}')