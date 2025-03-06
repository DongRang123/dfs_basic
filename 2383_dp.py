def process_stair(persons, stair):
    # persons: 해당 계단으로 배정된 사람들의 (x,y)
    # stair: (x, y, 길이)
    arrivals = []
    for p in persons:
        # 이동시간 = 맨해튼 거리, 도착 후 1분 대기 필요
        arrivals.append(abs(p[0]-stair[0]) + abs(p[1]-stair[1]) + 1)
    arrivals.sort()
    finish = [0] * len(arrivals)
    for i in range(len(arrivals)):
        if i < 3:
            finish[i] = arrivals[i] + stair[2]
        else:
            finish[i] = max(arrivals[i], finish[i-3]) + stair[2]
    return finish[-1] if finish else 0

def dfs(idx, group_a, group_b):
    global result
    if idx == len(person):
        time_a = process_stair(group_a, exit[0])
        time_b = process_stair(group_b, exit[1])
        result = min(result, max(time_a, time_b))
        return
    dfs(idx+1, group_a + [person[idx]], group_b)
    dfs(idx+1, group_a, group_b + [person[idx]])

for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    person = []
    exit = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                person.append((i, j))
            elif matrix[i][j] != 0:
                exit.append((i, j, matrix[i][j]))
    result = float('inf')
    dfs(0, [], [])
    print(f'#{test_case} {result}')
