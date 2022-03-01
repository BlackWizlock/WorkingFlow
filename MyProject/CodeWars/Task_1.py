def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))


test = "amxyz"
print(printer_error(test))
