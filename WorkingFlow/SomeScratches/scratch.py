def count_pixels(a: int, b: int, c: int = 1) -> int:
    return a * b * c


def main():
    a, b, c = map(int, input('Enter H x W x Pdensity :\t').split(", "))
    print(count_pixels(a, b, c))


if __name__ == '__main__':
    main()
