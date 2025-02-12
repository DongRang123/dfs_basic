#정점의 개수
V =7
#간선의 개수
E = 8
#간선 정보
'''
그래프의 상황에 따라서 간선 정보가 의미하는 바가 달라 질 수 있다.
1. 무방향 그래프인 경우, 간선의 정보가 한 방향에 대해서 주어지다러도
양쪽 모두로 이어 질 수 잇음을 의미한다
유방향 그래프인 경우, 당연하게도 주어진 간선 정보가 끝.
시작 정점 도착정점
   0        1
   0        2
   1        4
        ...
    5       6
'''

def dfs(node):
    print(node,end=' ')
    #조회를 시작했다. now번째 방문했다.
    visited[node] = True
    for next in range(V):
        #node 에서 next 방문
        if adj_matrix[node][next] and not visited[next]:
            dfs(next)

edge_data=[

    [3,5],
    [0,2],
    [1,3],
    [1,4],
    [2,4],
    [4,5],
    [0,1],
    [5,6]
]
# adj = {
#     0:[1,2],
#     1:[0,3,4],
#     2:[0,4],
#     3:[1,5],
#     4:[1,2,5],
#     5:[3,4,6],
#     6:[5]
# }

adj_matrix = [[0]*V for _ in range(V)]


for idx in range(E):
    # print(E,idx)

    #시작과 끝
    S, E = edge_data[idx]
    adj_matrix[S][E] = 1
    #무방향 그래프 이므로 반대도 똑같이 함.
    adj_matrix[E][S] = 1

# for adj in adj_matrix:
#     print(adj)
#node: 현재 방문한 노드의 값이 무엇인가?
#현재 해당 노드를 방문한 전적이 잇는지 체크하기 위한 리스트
visited = [False] *V
#내가 방문 가능한 대상인지만 골라먹기? xxxxxxxx
#모든 정점에 대해서 방문 가능한 여부는? adj_matrix에 표기해둿다.
for idx in range(V):
    #방문 여부 확인
    if visited[idx]:
        continue
    # 시작 정점 : idx -> 0으로 조회 시작
    dfs(0)