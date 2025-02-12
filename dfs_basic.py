tree = {
    'A':['B','C','D'],
    'B':['E','F'],
    'D':['G','H','I']

}

#node: 현재 방문한 노드의 값이 무엇인가?
def dfs(node):
    #현재 방문한 노드의 정보를 한줄로 출력
    print(node, end = ' ')
    #대박이네
    #파이썬의 for문은 비어있는 iterable 객체를 순회하라고 하면 아무것도 안함
    for child in tree.get(node, []):
        #자식들 기준으로 재 방문
        dfs(child)



dfs('A')