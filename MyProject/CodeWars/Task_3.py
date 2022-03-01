def compress(sentence):
    sentence = sentence.lower().split(" ")
    res = ""
    pos = 0
    count = -1
    for word in sentence:
        if sentence.index(word) != pos:
            res += str(sentence.index(word))
        else:
            res += str(pos)
            pos += 1
    return res


print(compress("The number 0 is such a strange number Strangely it has zero meaning"))
