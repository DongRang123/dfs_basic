import sys
sys.stdin = open("input.txt", "r")

isp = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0
}

icp = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 3
}

T = 10

for test_case in range(1, T + 1):

    N = int(input())

    matrix = list(input())
    stack = []
    what_calcu = ''
    after_num = 0
    for i in matrix:
        if not i.isnumeric():
            if i == ')':
                temp = ''
                while temp != '(':
                    temp = stack.pop()
                    what_calcu += temp
            else:
                if stack:
                    temp = stack.pop()
                    if (icp[i] > isp[temp]):
                        stack.append(temp)
                        stack.append(i)
                    else:

                        while stack and icp[i] < isp[temp]:
                            what_calcu += temp
                            temp = stack.pop()
                        stack.append(i)
                        what_calcu += temp
                else:
                    stack.append(i)
        else:
            what_calcu += i
    while stack != []:
        temp = stack.pop()
        what_calcu += temp
    # print(what_calcu)
    stack2 = []
    sum_num = 0
    # print(what_calcu)
    for what in what_calcu:
        # print(what)
        # print(stack2)
        if what.isnumeric():
            stack2.append(what)
        else:
            if what == '+':
                temp1 = stack2.pop()
                temp2 = stack2.pop()

                stack2.append(str(int(temp1) + int(temp2)))

            if what == '-':
                temp1 = stack2.pop()
                temp2 = stack2.pop()

                stack2.append(str(int(temp2) - int(temp1)))

            if what == '*':
                temp1 = stack2.pop()
                temp2 = stack2.pop()

                stack2.append(str(int(temp1) * int(temp2)))

            if what == '/':
                temp1 = stack2.pop()
                temp2 = stack2.pop()

                stack2.append(str(int(temp2) / int(temp1)))

    res = stack2.pop()

    print(f'#{test_case} {res}')