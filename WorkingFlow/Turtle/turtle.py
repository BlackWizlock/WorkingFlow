current_position = [0, 0]
n = int(input())
for i in range(n):
    tmp = str(input()).lower().split()
    if tmp[0] == 'север':
        current_position[1] += int(tmp[1])
    elif tmp[0] == 'юг':
        current_position[1] -= int(tmp[1])
    elif tmp[0] == 'восток':
        current_position[0] += int(tmp[1])
    elif tmp[0] == 'запад':
        current_position[0] -= int(tmp[1])
print(*current_position)
