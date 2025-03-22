def find_x(x):
    if parents[x] == x:
        return x
    parents[x] = find_x(parents[x])
    return parents[x]
 
def union(x,y):
    ref_x = find_x(x)
    ref_y = find_x(y)
 
    if ref_y == ref_x:
        return
 
    if ref_y < ref_x:
        parents[ref_x] = ref_y
    else:
        parents[ref_y] = ref_x
 
 
 
T= int(input())
 
for test_case in range(1,1+T):
    V, E = map(int, input().split())
    edges = []
    parents = [i for i in range(V+1)]
 
    for _ in range(E):
        u, v, w = map(int,input().split())
        edges.append((u,v,w))
    edges.sort(key = lambda x : x[2])
    cnt = 0
    result = 0
 
    for u,v,w in edges:
        if find_x(u) != find_x(v):
 
            union(u,v)
            cnt += 1
            result += w
 
            if cnt == V:
                break
 
    print(f'#{test_case} {result}')