T= int(input())
 
def dfs(idx,cnt):
    global result
    if cnt > result:
        return
 
    if idx >= len(matrix)+1:
        result = min(result,cnt)
        return
 
    for i in range(matrix[idx-1],0,-1):
        dfs(idx+i,cnt+1)
 
 
 
for test_case in range(1,1+T):
    matrix = list(map(int,input().split()))
    matrix = matrix[1:]
    result = len(matrix)+1
    dfs(1,-1)
    print(f'#{test_case} {result}')