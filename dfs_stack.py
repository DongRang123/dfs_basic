#정점의 개수
V =7
#간선의 개수
E = 8
#간선 정보
#재귀 함수가 아닌 stack 방식으로 진행
def dfs(node):
    #stack -> 다음 조사 대상 후보군을 모두 여기에 삽입
    stack = [node]
    visited[node] = True
    #stack에 값이 있는 동안 계속 탐색
    while stack:
        #가장 마지막에 들어온 값을 pop해서 조사대상으로 지정
        node = stack.pop()
        visited[node] = True
        print(node, end = ' ') #현재 방문한 대상 출력
        #현재 정점에서 이동 가능한 대상을 모두 조회
        for next in range(V):
            if adj_matrix[node][next] and not visited[next]:
                stack.append(next)


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

adj_matrix = [[0]*V for _ in range(V)]


for idx in range(E):
    S, E = edge_data[idx]
    adj_matrix[S][E] = 1
    adj_matrix[E][S] = 1


visited = [False] *V

for idx in range(V):

    if visited[idx]:
        continue
    dfs(0)

