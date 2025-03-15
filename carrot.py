T=int(input())
 
for test_case in range(1,1+T):
    N = int(input())
    matrix = list(map(int,input().split()))
    number = [0] *31
    result = float('inf')
    small = 0
    middle = 0
    large = 0
    for i in matrix:
        number[i] += 1
    #두번째 ㅅ작지점
    for second in range(2,31):
        if sum(number[1:second]) > N//2:
            continue
        if sum(number[1:second]) == 0:
            continue
        for third in range(second+1,31):
            if sum(number[second:third]) > N // 2:
                continue
            if sum(number[second:third]) == 0:
                continue
            if sum(number[third:]) > N // 2:
                continue
            if sum(number[third:]) == 0:
                continue
            small = sum(number[1:second])
            middle = sum(number[second:third])
            large = sum(number[third:])
            diff = max(abs(large-middle),abs(large-small),abs(middle-small))
            result = min(diff,result)
    if result == float('inf'):
        result = -1
    print(f"#{test_case} {result}")