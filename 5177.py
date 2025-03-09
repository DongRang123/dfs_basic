T = int(input())
def swap(a,b):
    a,b = b,a
 
 
for test_case in range(1,1+T):
    N = int(input())
    matrix = list(map(int,input().split()))
 
    heapq = [0]
    for i in range(len(matrix)):
        heapq.append(matrix[i])
        present_position = i+1
        if present_position == 1:
            continue
        while heapq[present_position//2] > heapq[present_position]:
            if present_position == 1:
                break
            heapq[present_position // 2],heapq[present_position] = heapq[present_position],heapq[present_position // 2]
            present_position = present_position//2
 
    length = len(heapq)-1
    res= 0
    while length != 1:
        length = length//2
        res+=heapq[length]
    print(res)
 
    print(f'#{test_case} {res}')