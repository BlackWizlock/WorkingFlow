def alphabet_position(text):
    text = text.lower()
    letters = [chr(i) for i in range(97, 123)]
    output = ""
    for letter in text:
        if letter in letters:
            output += str(letters.index(letter)+1) + " "
    return output[:-1]


alphabet_position("The sunset sets at twelve o' clock.")
