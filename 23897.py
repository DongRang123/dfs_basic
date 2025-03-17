T = int(input())


def binary_search(num):
    global cnt
    start = 0
    end = N-1
    check = None
    while start <= end:
        middle = (start + end) // 2
        if list_A[middle] == num:
            cnt += 1
            return 1

        if list_A[middle] <= num:
            start = middle + 1
            if check == "right":
                return
            check = "right"
        elif list_A[middle] > num:
            end = middle - 1
            if check == "left":
                return
            check = "left"
    return

for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    list_A = sorted(list(map(int, input().split())))
    list_B = list(map(int, input().split()))
    cnt = 0
    for i in list_B:
        binary_search(i)

    print(f'#{test_case} {cnt}')