# # games = int(input())
# games = 3
# lst_games = [
#     'Спартак;9;Зенит;10',
#     'Локомотив;12;Зенит;3',
#     'Спартак;8;Локомотив;15',
# ]
#
# dct_games = {
#     "name": "test",
#     "games": 0,
#     "wins": 0,
#     "draws": 0,
#     "lose": 0,
# }
#
# lst_new_games = [lst_games[i].split(";") for i in range(games)]
#
# print(lst_new_games)


n = int(input())
m = {}  # итоговый словарик
for i in range(n):
    str = input().split(';')
    d = {str[0]: str[1], str[2]: str[3]}
    winner = ''
    if int(str[1]) > int(str[3]):
        winner = str[0]
    elif int(str[1]) < int(str[3]):
        winner = str[2]
    for key in d.keys():
        if key not in m.keys():
            m.update({key: [0, 0, 0, 0, 0]})
        m.get(key)[0] += 1
        if key == winner:
            m.get(key)[1] += 1
        elif winner == '':
            m.get(key)[2] += 1
        else:
            m.get(key)[3] += 1
for key in m.keys():
    m.get(key)[4] = m.get(key)[1] * 3 + m.get(key)[2]
    print(key, end=':')
    for i in range(5):
        print(m.get(key)[i], end=' ')
    print()
