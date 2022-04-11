import re

usr_input = "Перезвони мне +7(926)232-213-23"
match = 0


def main():
    match = re.search(r"(?:\+|\-)?\d*\(\d*\)\d*-?\d*-?\d*", usr_input)
    if match:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
