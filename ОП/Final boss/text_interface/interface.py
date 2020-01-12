import sys
from thehotel.hotel import *
from text_interface import textu


class Base:

    def __init__(self):
        self.work = True
        self.errors = {
            '0x934b': '\n<><> Please, enter as an integer (pos). <><>\n',
            '0x18431': '\n<><> Please choose one of the following. <><>\n',
            '0x139': 'back',
            'exit': self.exitprogram,
            'help' : ''
        }
        self.stage = 'beginning'
        self.stagelist = {
           'beginning': self.beginning,
           'register': self.register,
           'login': self.login,
           'check': self.check,
           'notroomer': self.notroomer,
           'rent': self.rent,
           'infowin': self.infowin,
           'leave': self.leave,
           'expand': self.expand,
        }

        self.hotel = Hotel()
        self.user = None
        self.roomed = None

        self.run()
    
    def hasNumbers(self, inputString):
        return any(char.isdigit() for char in inputString)

    def helpu(self):
        print(textu.helpu)

    def exitprogram(self):
        self.work = False
        print('\n|||| Thank you for using vHotel, Goodbye!\n')

    def run(self):
        while self.work:
            self.stagelist[self.stage]()


    def wishudesu(self, options='', types='str', msg=''):
        if options:
            for i in options:
                print(f'-  {i}')
            op = input('>>> ').lower()
            if op == 'back':
                return '0x139'
            elif op == 'exit':
                return op
            elif op == 'help':
                self.helpu()
                return op
            if op in options:
                return op
            else:
                return '0x18431'

        elif msg:
            op = input(f'{msg}\n>>> ')
            if op.lower() == 'back':
                return '0x139'
            elif op.lower() == 'exit':
                return op
            elif op.lower() == 'help':
                self.helpu()
                return op
            r = self.checktype(types, op)
            if r and (types == 'pos'):
                op = int(op)
                return op
            elif not r:
                return '0x934b'
            else:
                return op

    def checktype(self, cl, op):
        if (cl == 'str'):
            return 1
        
        elif (cl == 'pos'):
            if op.isdigit():
                if int(op) > 0:
                    return 1
            else:
                return 0

    def beginning(self):
        print('|||| Hello and welcome to vHotel.\n'
              '|||| You can either register or login:')
        while True:
            desu = self.wishudesu(options=('register', 'login'))
            if desu in self.errors:
                if self.errors[desu] == 'back':
                    pass
                elif desu == 'exit':
                    self.errors[desu]()
                    break
                else:
                    print(self.errors[desu])

            else:
                self.stage = desu
                break
    
    def register(self):
        back = False
        print('|||| Oh, you are new?\n|||| Please give use the following information'
              ' in order to register or type "back" to return.\n')

        while not back:
            desu = self.wishudesu(msg='|| What\'s your name?\n')
            if desu in self.errors:
                if self.errors[desu] == 'back':
                    self.stage = 'beginning'
                    back = True
                    break
                elif desu == 'exit':
                    self.errors[desu]()
                    back = True
                    break
                else:
                    print(self.errors[desu])
            if self.hasNumbers(desu):
                print('|||| Do you really have nums in your name? No.\n')
            elif ' ' in desu:
                print('|||| Just in one word, please.\n')

            else:
                name = desu
                break

        while not back:
            desu = self.wishudesu(msg='|| What\'s your surname?\n')
            if desu in self.errors:
                if self.errors[desu] == 'back':
                    self.stage = 'beginning'
                    back = True
                    break
                elif desu == 'exit':
                    self.errors[desu]()
                    back = True
                    break
                else:
                    print(self.errors[desu])
            if self.hasNumbers(desu):
                print('\n|||| Do you really have nums in your surname? No.\n')
            elif ' ' in desu:
                print('\n|||| Just in one word, please.\n')

            else:
                surname = desu
                break

        while not back:
            desu = self.wishudesu(msg='|| What\'s your lastname?\n')
            if desu in self.errors:
                if self.errors[desu] == 'back':
                    self.stage = 'beginning'
                    back = True
                    break
                elif desu == 'exit':
                    self.errors[desu]()
                    back = True
                    break
                else:
                    print(self.errors[desu])
            if self.hasNumbers(desu):
                print('\n|||| Do you really have nums in your lastname? No.\n')
            elif ' ' in desu:
                print('\n|||| Just in one word, please.\n ')

            else:
                lastname = desu
                break

        while not back:
            desu = self.wishudesu(msg='What\'s your papers ID i.e Passport?', types='pos')
            if desu in self.errors:
                if self.errors[desu] == 'back':
                    self.stage = 'beginning'
                    back = True
                    break
                elif desu == 'exit':
                    self.errors[desu]()
                    back = True
                    break
                else:
                    print(self.errors[desu])

            else:
                regID = desu
                break
        
        while not back:
            desu = self.wishudesu(msg='|| If you want additional comment - it is right time for it.\n')
            if desu in self.errors:
                if self.errors[desu] == 'back':
                    self.stage = 'beginning'
                    back = True
                    break
                elif desu == 'exit':
                    self.errors[desu]()
                    back = True
                    break
                else:
                    print(self.errors[desu])

            else:
                comm = desu
                break
        
        if not back:
            info = [len(self.hotel.clientbase)+1, name, surname, lastname, regID, comm]
            self.hotel.clientbase.append(Client(*info))
            print('|||| You\'ve been registered. Welcome!\n')
            self.stage = 'beginning'
    
    def login(self):
        back = False
        self.user = None
        self.roomed = None
        ids = ''
        for i in self.hotel.clientbase:
            ids += str(i) + '\n'

        print(f'|||| Here are currently available users\n{ids}')
        while not back:
            desu = self.wishudesu(msg='|| Please enter the ID of the user you want to login\n', types='pos')

            if desu in self.errors:
                if self.errors[desu] == 'back':
                    self.stage = 'beginning'
                    back = True
                    break
                elif desu == 'exit':
                    self.errors[desu]()
                    back = True
                    break
                else:
                    print(self.errors[desu])
            else:
                for cl in self.hotel.clientbase:
                    if int(cl.id) == desu:
                        self.user = cl
                        self.stage = 'check'
                        back = True
                        break
                if not self.user:
                    print('\n|||| There is no such id. Enter another one.\n')

    def check(self):
        roomer = None
        self.hotel.check_roomers()
        for p in self.hotel.roomers:
            if self.user.id == p.clientInfo.id:
                roomer = True
                self.roomed = p
                self.stage = 'infowin'
        if not roomer:
            self.stage = 'notroomer'

    def notroomer(self):
        print(textu.nroom)
        while True:
            desu = self.wishudesu(options=('rent', 'back'))
            if desu in self.errors:
                if self.errors[desu] == 'back':
                    self.stage = 'login'
                    break
                elif desu == 'exit':
                    self.errors[desu]()
                    break
                else:
                    print(self.errors[desu])

            else:
                self.stage = desu
                break

    def rent(self):
        back = False
        text = ''
        for i in self.hotel.rooms:
            text += str(i) + '\n'
        print(f'|||| Here are all the rooms in vHotel. Take a look:\n{text}')

        while not back:
            desu = self.wishudesu(msg='|| Which one would you like?\n', types='pos')
            if desu in self.errors:
                if self.errors[desu] == 'back':
                    self.stage = 'check'
                    back = True
                    break
                elif desu == 'exit':
                    self.errors[desu]()
                    back = True
                    break
                else:
                    print(self.errors[desu])
            found = False
            for r in self.hotel.rooms:
                if r.number == desu:
                    found = True
                    room = r
                    break
            if found:
                if not r.busy:
                    break
                else:
                    room = None
                    print('\n|||| This room is busy. Pick another one.\n')
            else:
                print('\n|||| There is no such room. Try again.\n')

        while not back:
            desu = self.wishudesu(msg='|| For how many days?\n', types='pos')
            if desu in self.errors:
                if self.errors[desu] == 'back':
                    self.stage = 'check'
                    back = True
                    break
                elif desu == 'exit':
                    self.errors[desu]()
                    back = True
                    break

                else:
                    print(self.errors[desu])

            else:
                if desu < 1000000:
                    dur = desu
                    break
                else:
                    print('\n|||| You are living long, huh?\n Go away with that.\n')

        if not back:
            self.hotel.movein(self.user, room, dur)
            self.stage = 'check'
            print('\n|||| Welcome! Hope youll have good time here.\n')

    def infowin(self):
        print(f'|||| Roomer\'s information:\n\n{self.roomed.info()}\n\n|||| You can '
               'either Leave vHotel or Expand your rent (or go back)')

        while True:
            desu = self.wishudesu(options=('leave', 'expand', 'back'))
            if desu in self.errors:
                if self.errors[desu] == 'back':
                    self.stage = 'login'
                    break
                elif desu == 'exit':
                    self.errors[desu]()
                    break
                else:
                    print(self.errors[desu])
            else:
                self.stage = desu
                break

    def leave(self):
        self.hotel.kickout(self.roomed, self.user.id)
        print('\n|||| Was nice knowing you. Come back again.\n')
        self.stage = 'beginning'

    def expand(self):
        while True:
            desu = self.wishudesu(msg='|| For how many days?\n', types='pos')
            if desu in self.errors:
                if self.errors[desu] == 'back':
                    self.stage = 'check'
                    break
                elif desu == 'exit':
                    self.errors[desu]()
                    break

                else:
                    print(self.errors[desu])

            else:
                if desu < 1000000:
                    dur = desu
                    print(f'\n|||| You have succesfully expanded your rent for {dur} days.\n')
                    self.stage = 'check'
                    break
                else:
                    print('\n|||| You are living long, huh?\n Go away with that.\n')


def main():
    Base()