dxy = [(-1,-1),(-1,1),(1,1),(1,-1)] #왼쪽 위 부터 시계방향
T = int(input())
 
def dfs(current_postition, start_position,dessert_num,directions,map,last_direction):
 
    global result
    if directions == [True,True,True,True] and current_postition == start_position :
        # print(dessert_num)
        result = max(result,len(dessert_num)-1)
        # print(dessert_num)
        return
 
    for ind in range(len(dxy)):
        if (not directions[ind] and abs(ind-last_direction) != 2)or (ind == last_direction):
            nx = current_postition[0]+dxy[ind][0]
            ny = current_postition[1]+dxy[ind][1]
            if 0<=nx<N and 0<=ny<N:
                if not map[nx][ny] == -1:
                    dessert = map[nx][ny]
                    if dessert not in dessert_num or (nx,ny)==start_position:
                        if ind != last_direction:
                            map[nx][ny] = -1
                            directions[ind] = True
                            dfs((nx,ny),start_position,dessert_num+[dessert],directions,map,ind)
                            directions[ind] = False
                            map[nx][ny] = dessert
                        else:
                            map[nx][ny] = -1
                            dfs((nx, ny), start_position, dessert_num + [dessert], directions, map, ind)
                            map[nx][ny] = dessert
 
 
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    answer = []
    position_list = []
    result = 0
    for i in range(N):
        for j in range(N):
            list_a = list(matrix[_][:] for _ in range(N))
            direction = [False] *4
            dfs((i,j),(i,j),[list_a[i][j]],direction,list_a,-5)
    if result == 0:
        result = -1
    print(f'#{test_case} {result}')