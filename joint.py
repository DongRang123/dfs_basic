def make_set(x):
    p[x] = x #각 노드가 자기 자신을 부모로 가지도록 초기화
 
def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]
 
def union(x,y):
    px = find_set(x)
    py = find_set(y)
 
    if px != py:
        if rank[px] > rank[py]:
            p[py] = px
        elif rank[px] < rank[py]:
            p[px] = py
        else:
            p[py] = px
            rank[px] += 1
 
T= int(input())
 
for test_case in range(1,1+T):
    N ,M = map(int,input().split())
    p = [0] * (N + 1)  # 부모 노드 리스트 초기화
    rank = [0] * (N + 1)  # 랭크 리스트 초기화
    for i in range(1, N + 1):
        make_set(i)
    mat = list(map(int,input().split()))
 
    for i in range(M):
        union(mat[2*i],mat[2*i+1])
    result = set()
    for i in p:
        result.add(find_set(i))
 
 
    print(f'#{test_case} {len(result)-1}')