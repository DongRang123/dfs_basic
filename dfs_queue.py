from collections import deque

dxy = [[1,0],[0,1],[0,-1],[0,1]]

def dfs(depth, broken_cnt, matrix):
    global total_broken_block_cnt

    if depth == N:
        total_broken_block_cnt = max(total_broken_block_cnt,broken_cnt)
        return

    for w in range(W):
        """
        구슬을 w열에 던졌을때, matrix n*m 요기 블록판을 부숨
        1. 기존 블록판을 부수고, DFS로 넘기고, DFS을 빠져나오면 뭘 한다? 부순 블럭 복구
        2. 기존 블록판을 복사 -> 느린데 편함 그래서 일단 이거 해봄
        """

        arr = [x[:] for x in matrix]

        queue = deque()

        tmp_broken_cnt = 0

        for h in range(H):
            if arr[h][w]:
                queue.append((h,w))
                break

        while queue:
            x, y = queue.popleft()
            boom_cnt = arr[x][y]
            arr[x][y] = 0
            tmp_broken_cnt += 1

            for dx,dy in dxy:
                for dist in range(boom_cnt):
                    nx, ny = x + (dx*dist), y + (dy * dist)

                    if 0> nx or nx>= H or 0>ny or ny >= W: break

                    if not arr[nx][ny]: continue

                    if (nx,ny) in queue : continue

                    queue.append((nx,ny))

        for j in range(W):
            stack = []
            for h in range(H):
                if arr[h][j] != 0:
                    stack.append(arr[h][j])
                    arr[h][j] = 0
                
            for i in range(H-1,H-len(stack)-1,-1):
                arr[i][j] = stack.pop()

        
        dfs(depth+1,broken_cnt+tmp_broken_cnt,arr)


T = int(input())
for test_case in range(1,T+1):
    # N= '던질수 있는 구술의 갯수', W = 가로 H = 높이
    N,W,H = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(H)]

    '''
    최대한 많은 벽돌을 부수는것이 목표
    정답 - > 남은 벽돌의 개수

    1. 최대한 많은 벽돌을 부수는 경우
    2. 남은 벽돌의 개수가 적은 경우를 구하기

    주어진 총 벽돌의 갯수 - 최대로 부셨을때의 개수  = 정답
    '''

    total_block_cnt = 0
    for i in range(H):
        for j in range(W):
            if matrix[i][j] != 0:
                total_block_cnt += 1

    total_broken_block_cnt = 0

    '''
    bfs를 돌려야 하는데 파라미터를 뭐라고 해야할지 모르겠다,

    DFs->  재귀가 중단되어야함 즉 중단 트리거 들고가야함
    들고 가고 싶은 파라미터 (여태 부순 벽돌의 개수)

    1.파괴 되고 나서의 matrix
    2.
    '''
    dfs(0,0,matrix)



    result = total_block_cnt - total_broken_block_cnt

    print(f'#{test_case} {result}')