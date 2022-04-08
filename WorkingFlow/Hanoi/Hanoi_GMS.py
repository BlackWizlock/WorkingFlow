def print_hanoy(hanoy):
    max_disk_size = max([disk for pillar in hanoy for disk in pillar])
    disks_count = sum(map(len, hanoy))
    pillar_ident = (max_disk_size + max_disk_size % 2 + 2) // 2
    pillar_height = disks_count + 2

    # первые 2 строчки пустые
    empty_pillar_tip = ' ' * (pillar_ident - 1) + '|' + \
                       ' ' * (pillar_ident - 1) * 2 + '|' + \
                       ' ' * (pillar_ident - 1) * 2 + '|'
    print(empty_pillar_tip, empty_pillar_tip, sep='\n')

    for row in range(disks_count, 0, -1):
        row_string = ''

        for pillar in hanoy:
            if row <= len(pillar):
                disk_size = pillar[len(pillar) - row]
                row_string += ' ' * (pillar_ident - 1 - disk_size // 2) + \
                              '*' * disk_size + \
                              ' ' * (pillar_ident - 1 - disk_size // 2)
            else:
                row_string += ' ' * (pillar_ident - 1) + '|' + \
                              ' ' * (pillar_ident - 1)
        print(row_string)
    print()


def init_hanoy(disks=3):
    hanoy = [[], [], []]
    hanoy[0] = list(range(3, disks * 3, 2))
    return hanoy


def calc_steps_hanoy(hanoy):
    hanoy_steps = []

    def hanoy_save():
        hanoy_steps.append([el.copy() for el in hanoy])

    def step(disks, pillar_from, pillar_to, pillar_buf):
        if disks == 0:
            return
        step(disks - 1, pillar_from, pillar_buf, pillar_to)
        hanoy[pillar_to].insert(0, hanoy[pillar_from].pop(0))
        hanoy_save()
        step(disks - 1, pillar_buf, pillar_to, pillar_from)

    disks = sum(map(len, hanoy))

    hanoy_save()
    step(disks, 0, 2, 1)

    return hanoy_steps


hanoy_steps = calc_steps_hanoy(init_hanoy(5))

for hanoy in hanoy_steps:
    print_hanoy(hanoy)
