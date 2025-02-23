def comb(arr,n):
    result = []
    if n ==1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in comb(arr[i+1:],n-1):
            result.append([elem]+rest)
    return result
T = 10
for test_case in range(1, T + 1):