import sys
sys.stdin = open("input.txt", "r")

from collections import deque

#1. 전체 공간을 복사해서 각 공간의 좌표마다 시작지점에서 얼마나 이동했나를 표기
#장점 : 모든 목적지의 최단거리를 알 수 있다.
#단점 : 메모리 2배 차지한다.
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def get_road_move_time():
                #x,y,acc
    queue = deque([(0,0,0)])
    visited = [[False] * M for _ in range(N)]
    while queue:
    #queuerk
        x, y, dist = queue.popleft()
        for k in range(4):
            next_x = x + dx[k]
            next_y = y + dy[k]
            next_dist = dist + 1
            #1. 리스트의 범위를 벗어나지 않아야한다
            if 0<= next_x< N  and 0 <= next_y < M and data[next_x][next_y]:
                queue.append((next_x, next_y,next_dist))

                if next_x == N-1 and next_y == M-1:
                    return next_dist
    return -1
N, M = map(int,input().split())
data = [list(map(int,input())) for _ in range(N)]



#최종 결과값
 # 문제에서 요구하는 값을 넣으면 된다.
#함수 이름을 DFS or BFS로 정의하는 건 권장하지 않음
#정확한 용도를 작성 해달라
#함수의 역할 -> 이동하는데 드는 최소 비용을 구하는 함수
#이 문제에서는 출발 정점의 xy 좌표가 고정
result = get_road_move_time()
print(result)