def mapper(data: dict, data_map: dict) -> dict:
    new_data = {}
    for key, value in data.items():
        if key in data_map:
            new_data[data_map[key]] = value
        else:
            new_data[key] = value
    return new_data


# return mapped_data

data_map = {}

usr_db = {"f": "Ivanov", "i": "Ivan", "o": "Ivanovich"}


def main():
    while True:
        d_key, d_value = str(input("Enter Key: \t")), str(input("Enter value: \t"))
        if d_key == "" or d_value == "":
            break
        else:
            data_map[d_key] = d_value
    print(mapper(usr_db, data_map))


if __name__ == "__main__":
    main()
