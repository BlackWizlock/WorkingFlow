usr_str = str(input()).lower().split()
usr_dct = {word: usr_str.count(word) for word in usr_str}

for key, value in usr_dct.items():
    print(key, value)
