def find_needle(haystack):
    # your code here
    return "found the needle at position {}".format(haystack.index("needle"))


print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
