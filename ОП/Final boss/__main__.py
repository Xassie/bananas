""" Python 3.7.4
    SShpakov-ki19
    Вариант 27
"""

import argparse

def cmd():
        parser = argparse.ArgumentParser(description='Choose the way of visualisation.')
        parser.add_argument('N', action='store', help='Graphic or text visualisation')
        R = parser.parse_args()
        return R.N

def visint():
    pass

def textint():
    import text_interface.interface as inf
    inf.Interface()

def main():
    op = cmd()
    if op.lower() == 'graphic':
        visint()
    elif op.lower() == 'text':
        textint()
    


if __name__ == '__main__':
    main()