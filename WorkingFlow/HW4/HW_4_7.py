MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


# user_input = input("Add some Morse code line \(usable symbols only * and -\)")

# DECODE
user_input = "- .... .. ... .. ... -.. . -.-. --- -.. . -.."
user_input = user_input.split()
for i in user_input:
    print(list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(i)], end="")

print("\n")

# CODE
user_tobe_coded = "TESTLINE"
for i in user_tobe_coded:
    print(MORSE_CODE_DICT[i], end=" ")
