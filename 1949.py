dxy = [(-1,0),(0,1),(1,0),(0,-1)]
 
def dfs(idx,x,y,visited_map,prev_value,chance):
 
    global result
 
 
    for dx,dy in dxy:
        nx = x+dx
        ny = y+dy
        if 0<=nx<N and 0<=ny<N:
            if visited_map[nx][ny] != -99:
                if visited_map[nx][ny]< prev_value:
                    save_point = visited_map[nx][ny]
                    visited_map[nx][ny]= -99
                    dfs(idx+1,nx,ny,visited_map,save_point,chance)
                    visited_map[nx][ny] = save_point
                elif chance == True and visited_map[nx][ny]-prev_value<K:
                    save_point = visited_map[nx][ny]
                    visited_map[nx][ny] = -99
                    dfs(idx + 1, nx, ny, visited_map, prev_value-1, False)
                    visited_map[nx][ny] = save_point
 
    result = max(idx,result)
    return
 
T= int(input())
 
for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
 
    highest_position = []
    #가장 높은 곳 좌표 찾기
    max_num = 0
    for i in range(N):
        for j in range(N):
            max_num = max(max_num,matrix[i][j])
    for i in range(N):
        for j in range(N):
            if max_num == matrix[i][j]:
                highest_position.append((i,j))
    result = 0
    for x,y in highest_position:
        visit_map = [row[:] for row in matrix]
        a = visit_map[x][y]
        visit_map[x][y] = -99
        dfs(1,x,y,visit_map,a,True)
 
 
    print(f'#{test_case} {result}')