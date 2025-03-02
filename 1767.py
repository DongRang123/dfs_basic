T = int(input())
 
# 기존과 같은 방향: 왼, 아래, 오른, 위
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
 
def dfs(index, connected, length):
    global max_core, min_length, cores, board, N
 
    # 모든 코어를 처리했다면 결과 갱신
    if index == len(cores):
        if connected > max_core:
            max_core = connected
            min_length = length
        elif connected == max_core:
            min_length = min(min_length, length)
        return
 
    # 가지치기: 남은 코어 모두 연결해도 현재 최대 연결 코어 수 미달이면 중단
    if connected + (len(cores) - index) < max_core:
        return
 
    r, c = cores[index]
    # 현재 코어에 대해 4방향 전선 연결 시도
    for d in range(4):
        nr, nc = r, c
        path = []
        possible = True
        # 방향 d로 이동하며 전선 경로를 확인
        while True:
            nr += direction[d][0]
            nc += direction[d][1]
            # 보드 밖에 도달하면 연결 성공
            if not (0 <= nr < N and 0 <= nc < N):
                break
            # 이미 코어나 전선이 있으면 연결 불가
            if board[nr][nc] != 0:
                possible = False
                break
            path.append((nr, nc))
        # 연결 가능한 경우에만 진행 (전선이 한 칸 이상 필요)
        if possible and len(path) > 0:
            # 전선 표시 (값 2)
            for (pr, pc) in path:
                board[pr][pc] = 2
            dfs(index + 1, connected + 1, length + len(path))
            # 백트래킹으로 전선 제거
            for (pr, pc) in path:
                board[pr][pc] = 0
 
    # 현재 코어를 연결하지 않는 경우 (연결 불가 또는 연결 포기)
    dfs(index + 1, connected, length)
 
for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    # 가장자리 코어는 이미 연결된 것으로 처리하므로, 내부 코어만 cores 리스트에 추가
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                    continue
                cores.append((i, j))
 
    max_core = 0
    min_length = float('inf')
    dfs(0, 0, 0)
    # 만약 연결한 코어가 없으면 문제 조건에 따라 0 출력 (여기서는 wire 길이 0)
    if min_length == float('inf'):
        min_length = 0
    print(f'#{t} {min_length}')