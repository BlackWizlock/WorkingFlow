usr_input = ["(a+b)", "()()))sdf)", "))", ""]


def br_cheak(ln: str) -> bool:
    for i in ln:
        if i == "(" or i == ")":
            continue
        else:
            ln = ln.replace(i, '')
    while '()' in ln or '[]' in ln or '{}' in ln:
        ln = ln.replace('()', '')
        ln = ln.replace('[]', '')
        ln = ln.replace('{}', '')

    # Возвращаем True, если text с пустой строкой
    if any([x in ln for x in ["(", ")"]]):
        return False
    else:
        return True


def main():
    for word in usr_input:
        print(br_cheak(word))


if __name__ == '__main__':
    main()
