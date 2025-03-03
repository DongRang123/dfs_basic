T = int(input())
#갯수 찾기
def calcu(house_list,K1):
    max_cnt = 0
    for ii in range(N):
        for jj in range(N):
            cnt = 0
            for houses in house_list:
                if (abs(ii-houses[0])+abs(jj-houses[1])) <= K1-1:
                    cnt += 1
            max_cnt = max(max_cnt,cnt)
    return max_cnt
 
 
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    houses = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                houses.append((i,j))
 
    #Krange 정하기
    k_max= 1
    while len(houses)*M > k_max*k_max +(k_max-1)*(k_max-1):
        k_max += 1
 
    profit_max = 0
    result = 0
    for kk in range(k_max,-1,-1):
        house_max = calcu(houses,kk)
        profit = M*house_max - (kk*kk + (kk-1)*(kk-1))
        if profit>=0:
            result = house_max
            break
 
 
    print(f'#{test_case} {result}')