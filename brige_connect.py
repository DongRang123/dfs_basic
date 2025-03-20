dxy = [[0,1],[0,-1],[1,0],[-1,0]]
 
INF = int(21e8)
def find_parents(x):
    if parents[x] == x:
        return x
    parents[x] = find_parents(parents[x])
    return parents[x]
 
def union(x,y):
    ref_x = find_parents(x)
    ref_y = find_parents(y)
 
    if ref_y == ref_x:
        return
 
    if ref_y>ref_x:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y
 
 
 
T= int(input())
 
for test_case in range(1,1+T):
    N = int(input())
    position_x = list(map(int,input().split()))
    position_y = list(map(int,input().split()))
    E = float(input())
    parents = [i for i in range(N)]
    edges = []
    for i in range(N):
        for j in range(i+1,N):
            edges.append((i,j,(position_x[i]-position_x[j])**2+(position_y[i]-position_y[j])**2))
 
    edges.sort(key=lambda x:x[2])
 
    cnt = 0
    result = 0
 
    for u,v,w in edges:
        if find_parents(u) != find_parents(v):
            union(u,v)
            cnt+=1
            result+=w
 
            if cnt == N-1:
                break
 
    print(f'#{test_case} {int(round(result*E,0))}')