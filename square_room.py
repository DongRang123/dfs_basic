from collections import deque
T = int(input())
dxy = [[1,0],[0,1],[-1,0],[0,-1]]


for test_case in range(1,1+T):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    length =1
    min_value = float('inf')
    new_matrix = [[0]*N for _ in range(N)]
    idx = 1
    Queue = deque()
    for i in range(N):
        for j in range(N):
            if new_matrix[i][j] == 0:
                Queue.append((i,j))
                new_matrix[i][j] = idx
                #실행횟수
                num = 1
                min_num = matrix[i][j]
            while Queue:
                spot = Queue.popleft()
                for jj in range(4):
                    nx = spot[0] + dxy[jj][0]
                    ny = spot[1] + dxy[jj][1]
                    if (0<=nx<N) and (0<=ny<N):
                        if abs(matrix[nx][ny] - matrix[spot[0]][spot[1]]) == 1:
                            if new_matrix[nx][ny] == 0:
                                if (nx,ny) not in Queue:
                                    new_matrix[nx][ny] = idx
                                    num += 1
                                    Queue.append((nx,ny))
                                    min_num = min(min_num,matrix[nx][ny])
            if num > length:
                length = num
                min_value = min_num
            elif num == length:
                min_value = min(min_num, min_value)
            idx += 1



    print(f"#{test_case} {min_value} {length}")