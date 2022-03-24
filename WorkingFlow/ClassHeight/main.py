# Файл состоит из набора строк, каждая из которых представляет собой три поля:
# Класс Фамилия Рост
dct_container = {cl: [0, 0] for cl in range(1, 12)}
info_container = list()

with open('dataset_3380_5.txt', 'r') as of:
    for line in of:
        dct_container[int(line.strip().split("\t")[0])][1] += int(line.strip().split("\t")[2])
        dct_container[int(line.strip().split("\t")[0])][0] += 1
with open('output.txt', 'w') as ofw:
    for k, v in dct_container.items():
        ofw.write(f'{str(k)} ')
        ofw.write(f'{str(v[1] / v[0]) if v[0] else "-"}\n')
