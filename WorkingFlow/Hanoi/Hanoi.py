draw_freee = "   |   "
draw_small = "  ***  "
draw_middd = " ***** "
draw_biggg = "*******"

game_matrix = [
    [draw_small, draw_freee, draw_freee],
    [draw_middd, draw_freee, draw_freee],
    [draw_biggg, draw_freee, draw_freee]
]


def status_changer(x, y, state):

    if state == 1:
        game_matrix[x][y] = draw_small
    if state == 2:
        game_matrix[x][y] = draw_middd
    if state == 3:
        game_matrix[x][y] = draw_biggg
    if state == 0:
        game_matrix[x][y] = draw_freee
    draw_loop()


def draw_loop():
    for i in range(3):
        print()
        for j in range(3):
            print(game_matrix[i][j], end="")


def main():
    draw_loop()
    status_changer(2, 1, 1)
    status_changer()


if __name__ == '__main__':
    main()
