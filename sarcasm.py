import re
import sys

import pyperclip


def sarcasm_bot(sentence):
    characters = {}
    regex = "[A-Za-z]"
    specials = r"[!:;@#$%^&*()?'\"]"
    complete = []

    x = 0
    for i in sentence:
        characters[x] = i
        x += 1

    x = 0
    for t in characters:
        if re.match(r"\s", characters[t]):
            complete.append(' ')
        if re.search(specials, characters[t]):
            complete.append(re.search(specials, characters[t]).group())
        if re.match(regex, characters[t]):
            if t % 2 == 0:
                complete.append(str(characters[t]).lower())
                x += 1
            else:
                complete.append(str(characters[t]).upper())
                x += 1

    complete[0:complete.__len__()] = [''.join(complete[0:complete.__len__()])]
    pyperclip.copy(complete[0])
    return complete[0]


if sys.argv[1]:
    print(sarcasm_bot(sys.argv[1]))
    print('Copied to Clipboard')
else:
    print(sarcasm_bot(input("Enter sentence: ")))
    print('Copied to Clipboard')
