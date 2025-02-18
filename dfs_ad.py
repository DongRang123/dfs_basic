def dfs(idx,sequence, cnt):
    global max_cnt
    if idx == N:
        max_cnt = max(max_cnt, cnt)
        return
    if cnt + remaining_max[idx] < max_cnt:
        return
    if sequence == 1:
        dfs(idx+1, 1, cnt+list_a[idx]-P)
    else:
        dfs(idx+1, 1, cnt+list_a[idx])

    if sequence == 2:
        dfs(idx + 1, 2, cnt + list_b[idx] -P)
    else:
        dfs(idx + 1, 2, cnt + list_b[idx])

T = int(input())  # 테스트 케이스 개수
for test_case in range(1, T + 1):
    N, P = map(int,input().split())
    list_a = list(map(int,input().split()))
    list_b = list(map(int, input().split()))
    idx = 0
    sequence = -1
    cnt = 0
    max_cnt = 0

    remaining_max = [0] * (N)
    for i in range(N - 1, -1, -1):
        if i +1 <N:
            remaining_max[i] = max(list_a[i],list_b[i]) + remaining_max[i+1]
        else:
            remaining_max[i] = max(list_a[i],list_b[i])
    dfs(idx, sequence, cnt)

    print(f"#{test_case} {max_cnt}")