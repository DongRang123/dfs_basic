import sys
sys.stdin = open("input.txt", "r")

def dfs(idx, matrix ,point):

    global res

    if idx == 2:
        # print(res)
        res = max(point,res)
        return

    for i in range(N):
        for j in range(N-M+1):
            arr = [x[:] for x in matrix]
            point_t = point
            sub_matrix = []
            keep_going = True
            # print(i,j)
            for m in range(M):
                if arr[i][j+m] == -1:
                    keep_going = False
                    sub_matrix = []
                    break
                else:
                    sub_matrix.append(arr[i][j+m])
            # print(sub_matrix)
            if keep_going :

                point_t += best_score(sub_matrix)
                for mm in range(M):
                    # print(j,m)
                    arr[i][j+mm] = -1
                # print(arr)
                dfs(idx+1, arr, point_t)


def best_score(matrix1):
    mat = []
    sub_point = 0
    for oo in range(1<<M):
        sub_mat = []
        for jj in range(M):
            if oo & (1<<jj):
                # print('j',j)
                # print('len',len(matrix1))
                sub_mat.append(matrix1[jj])
        mat.append(sub_mat)
    # print(mat)
    for z in mat:
        sub_point_t = 0
        if sum(z) > C:
            continue
        else:
            for zz in z:
                sub_point_t += pow(zz,2)
        sub_point = max(sub_point_t,sub_point)
    return sub_point

T = int(input())
for test_case in range(1, T + 1):
    N,M,C = map(int,input().split())
    res = 0
    matrix = [list(map(int,input().split())) for _ in range(N)]
    dfs(0,matrix, 0)
    print(f'#{test_case} {res}')

