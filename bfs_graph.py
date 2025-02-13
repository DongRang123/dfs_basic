import sys

# sys.stdin = open("input.txt", "r")

from collections import deque

def BFS(node_index):
    #q가 존자하는 동안. -> Q를 생성
    queue = deque([node_index])
    visited[node_index] = True
    while queue:
        now_idx =queue.popleft()
        result.append(now_idx)
        #현재 노드가 가진 모든 자식들을 대해서 조사
        for neighbor_idx in graph[now_idx]:
            if not visited[neighbor_idx]:
                queue.append(neighbor_idx)
                visited[neighbor_idx] = True
    return result



#그래프 인접 리스트
graph = {
    'A':['B','C'],
    'B':['E','F','D'],
    'C':['A','E'],
    'D':['B','F'],
    'E':['B','C','F'],
    'F':['D','E','G'],
    'G':['F']
}
#너비 운선 탐색 -> 표시
visited = {key: False for key in graph}

result =[]
# BFS('A')
# print(result)

for node in graph:
    if node == 'F':
        BFS(node)
print(*result)
