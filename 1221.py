T = int(input())

def check(check_list,W_t):
    # 연속된건지 확인하는 로직:
    for j in range(W_t):
        cnt = 1
        valid =False
        for i in range(1,D):
            if check_list[i][j] == check_list[i-1][j]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K:
                valid = True
                break
        if not valid:
            return False
    return True

def dfs(lists_q, idx,change):
    global result
    #종료 조건

    #최소 갯수 세는 거임
    if change>=result:
        return

    #끝까지 도달시 조건 찾기 실패
    if idx == D:
        if check(lists_q, W):
            result = min(result, change)
            return
        return

    #K번 연속해서 바꾸면 무조건 통과이므로
    if change >= K:
        return

    #최솟값 로직인거지 이게
    if check(lists_q, W):
        result = min(result,change)
        return

    lists_q_copy_1 = [x[:] for x in lists_q]
    lists_q_copy_2 = [x[:] for x in lists_q]
    #idx행 A로 바꾸기
    lists_q_copy_1[idx] = [0] * W
    dfs(lists_q_copy_1, idx+1,change+1)

    #idx행 B로 바꾸기
    lists_q_copy_2[idx] = [1] * W
    dfs(lists_q_copy_2, idx+1,change+1)

    #바꾸지 않고 진행
    dfs(lists_q,idx+1,change)

for test_case in range(1, T + 1):
    D,W,K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(D)]
    result = K
    dfs(matrix,0,0)

    print(f'#{test_case} {result}')