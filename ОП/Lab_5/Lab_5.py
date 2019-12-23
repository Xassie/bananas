""" Python 3.7.4
Шпаков Станислав
Вариант 25

Coding program.
Raw text should be in text.txt
The result will be in result.txt
"""

import argparse

SHIFT = 3
CODES = {
    'en' : 26,
    'ru' : 32,
}


def listed(value):
    """ New type just to make it easier """

    if value.lower() not in ['encode', 'decode',]:
        raise argparse.ArgumentTypeError("Your option is not listed")
    return value


def cmd():
    parser = argparse.ArgumentParser(description='Which operation to perform?')
    parser.add_argument('N', action='store', type=listed, help='Encode or decode.')
    R = parser.parse_args()
    return R.N.lower()

def decode(ccode, slide, lang):
    """ Decoding mechanism.
        Shifts given element SHIFT(3) elements forth.
    """

    if slide:
        alp = CODES[lang]
        ccode -= slide - SHIFT
        if ccode >= alp:
            ccode -= alp
    return chr(ccode + slide)
    

def test_decoding():
    assert decode(102, 97, 'en') == 'i'
    assert decode(76, 65, 'en') == 'O'
    assert decode(1053, 1040, 'ru') == 'Р'

def encode(ccode, slide, lang):
    """ Encoding mechanism
        Shifts given element SHIFT(3) elemens back
    """

    if slide:
        alp = CODES[lang]
        ccode -= SHIFT + slide
        if ccode < 0:
            ccode += alp
    return chr(ccode + slide)

def test_encoding():
    assert encode(84, 65, 'en') == 'Q'
    assert encode(104, 97, 'en') == 'e'
    assert encode(1089, 1072, 'ru') == 'о'
    assert encode(99, 97, 'en') == 'z'
    assert encode(1074, 1072, 'ru') == 'я'

def determine(character):
    """ Determine char type.
        Checks to what group given character belongs.
        It returns the language and the slide you'll need to perform
    """

    code = ord(character)
    if code == 1105:
        code = 1077
    elif code == 1025:
        code = 1045
    if (65 <= code <= 90):
        lan = 'en'
        slide = 65
    elif (97 <= code <= 122):
        lan = 'en'
        slide = 97
    elif (1040 <= code <= 1071):
        lan = 'ru'
        slide = 1040
    elif (1072 <= code <= 1103):
        lan = 'ru'
        slide = 1072
    else:
        lan = None
        slide = 0
    
    return code, slide, lan


def test_determination():
    assert determine('T') == (84, 65, 'en')
    assert determine('h') == (104, 97, 'en')
    assert determine('с') == (1089, 1072, 'ru')
    assert determine('c') == (99, 97, 'en')

def fread():
    with open('./text.txt', "r") as file:
        text = file.readlines()
    return text

def fwrite(res):
    with open('./result.txt', "w") as file:
        file.write(res)

def main():
    message = fread()
    result = ''
    for line in message:
        for i in line:
            result += OPTION[cmd()](*determine(i))
    fwrite(result)


OPTION = {
    'decode' : decode,
    'encode' : encode,
}

if __name__ == "__main__":
    main()
