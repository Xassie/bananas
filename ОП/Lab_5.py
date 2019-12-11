""" Python 3.7.4
Шпаков Станислав
Вариант 25
"""

import argparse

SHIFT = 3
CODES = {
    'en' = 26
    'ru' = 33
}


def listed(value):
    if value.lower() not in ['encode', 'decode',]:
        raise argparse.ArgumentTypeError("Your option is not listed")
    return value


def cmd():
    parser = argparse.ArgumentParser(description='Which operation to perform?')
    parser.add_argument('N', action='store', type=listed, help='Encode or decode.')
    R = parser.parse_args()
    return R.N.lower()

def decode(ccode, slide, lang):
    alp = CODES[lang]
    ccode -= slide + SHIFT
    if ccode <= 0:
        ccode += alp
    return chr(ccode + slide)   
    

def test_decoding():
    pass

def encode(ccode, slide, lang):
    if slide:
        alp = CODES[lang]
        ccode += SHIFT - slide
        if ccode >= alp:
            ccode -= alp
    return chr(ccode + slide)

def test_encoding():
    pass

def determine(character):

    code = ord(character)
    if (65 <= code <= 90):
        lan = en
        slide = 65
    elif (97 <= code <= 122)
        lan = en
        slide = 97
    elif (1040 <= code <= 1071):
        lan = ru
        slide = 1040
    elif (1072 <= code <= 1103):
        lan = ru
        slide = 1072
    else:
        lan = None
        slide = 0
    
    return code, lan, slide


def test_determination():
    pass

def read():
    with open('text.txt', "r") as file:
        text = file.readlines()
    return text

def write(res):
    with open('result.txt', "w") as file:
        file.write(res)

def main():
    message = read()
    result = ''
    for i in message:
        result += OPTION[cmd()](i)
    write(result)


OPTION = {
    'decode' = decode
    'encode' = encode
}

if __name__ == "__main__":
    main()