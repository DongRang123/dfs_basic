# 기본
import sys
sys.stdin = open("sample_input.txt")


def dfs(cx, cy, depth, visited, is_hint):
    global res

    c_h = arr[cx][cy]  # 현재 좌표의 높이
    res = max(res, depth)  # 여태까지 나온 등산로의 길이를 매번 갱신 ( 안되면 말고 )

    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy
        # 범위를 벗어났는 지 확인 => 벗어났으면 continue
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        # 방문한 적이 있으면 패스
        if visited[nx][ny]: continue

        next_h = arr[nx][ny]  # 이동하려고 하는 곳의 높이

        # 낮은 지형이면 그냥 들어가면 돼요
        if c_h > next_h:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, visited, is_hint)
            visited[nx][ny] = False

        # 같거나 높은 지형인 경우에는?? 이제 힌트가 있으면 깍아야 한다.
        if c_h <= next_h and is_hint and next_h - K < c_h:
            arr[nx][ny] = c_h - 1
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, visited, False)
            visited[nx][ny] = False
            arr[nx][ny] = next_h



dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    _visited = [[False] * N for _ in range(N)]
    res = 0

    # 1. 가장 높은 봉우리의 높이를 찾자. 2차원 배열에서 가장 높은 높이 값
    max_h = max(max(row) for row in arr)

    # 2. 가장 높은 곳은 여러 곳일 수 있다.
    # 가장 높은 봉우리를 찾자.
    max_h_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_h:
                max_h_list.append([i, j])

    # 가장 높은 봉우리 목록에서 하나하나씩 DFS 탐색을 시작하자.
    for max_h_x, max_h_y in max_h_list:
        # 이 지점을 처음 시작부분으로 해서 DFS 로 가능한 모든 경우를 찾아보자.
        # 시작하는 지점을 방문처리한다.
        _visited[max_h_x][max_h_y] = True
        """
        DFS 작성할때 파라미터를 뭐로 할까? 
        - 뭐할지모르겠다? 그러면 변수 다 넣어요 
        - 내가 누적해서 가져가고 싶은 값이 뭐지 ?? 
        (x,y 좌표, 여태까지 만들어진 등산로 길이, 공사 기회가 남아 있는지, 방문 여부 
        """
        dfs(max_h_x, max_h_y, 1, _visited, True)

        # 원상복구 시킨다 => why ??? 다른 지점에서도 다시 DFS 시작할거기때문에 초기화해줘야하는거다.
        _visited[max_h_x][max_h_y] = False

    print(f"#{test_case}")
