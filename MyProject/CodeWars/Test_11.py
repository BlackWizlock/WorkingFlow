def pig_it(words):
    output = ""
    for word in words.split(sep=" "):
        word = (word + word[0:1])
        output += word[1:] + "ay "
    return output.rstrip(" ")


pig_it("Pig words here")