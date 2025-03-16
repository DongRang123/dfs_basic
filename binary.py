T = int(input())
 
for test_case in range(1, T + 1):
    N = float(input())
    cnt = 0
    res = ''
    while N != 0.0 and cnt <12:
        N = N *2
        if N>=1:
            N = N-1
            res = res +'1'
        else:
            res = res + '0'
        cnt += 1
    if cnt >= 12 and N != 0.0:
        res = 'overflow'
 
    print("hello")
    print(f'#{test_case} {res}')