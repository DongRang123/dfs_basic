import sys

# sys.stdin = open("input.txt", "r")

from collections import deque

def BFS(node_index):
    #q가 존자하는 동안. -> Q를 생성
    queue = deque([node_index])
    result = []
    while queue:
        now_idx =queue.popleft()
        result.append(now_idx)
        #현재 노드가 가진 모든 자식들을 대해서 조사
        for child_idx in tree[now_idx][1:]:
            queue.append(child_idx)
    return result



#0번 인덱스를 이용할 것인지
#가가 노드가 가지고 있을 값이 중요하다면?
# 자식 노드들의 정보는 어떻게 표현할 것인가?
tree = [0,
        ['A',2,3,4],
        ['B',5,6],
        ['C'],
        ['D',7,8,9],
        ['E'],['F'],['G'],['H'],['I']
        ]
# tree = {
#     'A':['B','C','D'],
#     'B':['E','F'],
#     'D':['G','H','I']
# }

result = BFS(1)
print(result)

