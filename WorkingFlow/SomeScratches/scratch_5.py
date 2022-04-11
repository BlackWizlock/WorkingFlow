def coin_searching(amount: int, tpl: dict):
    for k, v in tpl.items():
        tpl[k] = amount // k
        amount -= tpl[k] * k
    print(tpl)

def main():
    usr_input = int(input())
    # usr_input = 27
    usr_tpl_input = {int(x): 0 for x in input().split(", ")}
    # usr_tpl_input = {
    #     10: 0,
    #     5: 0,
    #     2: 0,
    #     1: 0,
    # }
    coin_searching(usr_input, usr_tpl_input)


if __name__ == '__main__':
    main()
