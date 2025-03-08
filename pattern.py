T = int(input())
pattern = {
    '001101' :0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9,

}
hex_to_bin ={
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}


for test_case in range(1,1+T):
    hexa = input().strip()
    new = ''
    for i in hexa:
        new += hex_to_bin[i]
    for z in range(len(new)-1,0,-1):
        if new[z] == '1':
            break

    for i in range(6):
        if (z - i) % 6 == 0:
            break
    new = new[i+1:z+1]
    print(new)
    result = []
    for i in range(0,len(new),6):
        result.append(str(pattern[new[i:i+6]]))

    print(f'#{test_case} {" ".join(result)}')