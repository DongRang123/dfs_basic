T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
 
for test_case in range(1, T + 1):
    N,T = map(int,input().split())
 
    matrix = []
    for i in range(1,N+1):
        matrix.append(i)
    over = int(len(matrix)*0.37)
    perfect = int(len(matrix)*0.5)
 
    #셔플 시작
    for i in range(T):
        #오버핸드셔플
        matrix = matrix[len(matrix)-over:]+matrix[:len(matrix)-over]
 
        #퍼펙트 셔플
        perfect_a = matrix[:len(matrix)-perfect]
        perfect_b = matrix[len(matrix)-perfect:]
 
        new_matrix = []
 
        for z in range(perfect):
            new_matrix.append(perfect_a[z])
            new_matrix.append(perfect_b[z])
 
 
        if N %2 ==1:
            new_matrix.append(perfect_a[-1])
 
        matrix = new_matrix
    result = []
    for i in range(N):
        result.append(str(matrix[i]))
 
    print(f'#{test_case} {" ".join(result)}')