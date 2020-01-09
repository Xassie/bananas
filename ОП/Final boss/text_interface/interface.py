from thehotel.hotel import *


class Interface:

    def __init__(self):
        self.run = True
        self.start()
        self.current_user = None
        self.stage = 'onboot'
        self.options ={
            'onboot' : {
                'login' : self.login,
                'register' : self.register,
            },
            'logged' : {
                
            }
        }


    def start(self):
        self.hotel = Hotel()
        while self.run:
            self.choose_option()


    def choose_option(self):
        if self.stage == 'onboot':
            print('Hello. Welcome to our vHotel.\n'
                'You can whether "login" or "register".')
        while self.run:
            opt = input('>>> ').lower()
            if opt == 'exit':
                self.run = False
                break
            if opt in self.options[self.stage]:
                self.options[self.stage]()
                break

    def register(self):
        print('Please enter your Name, Surname, Lastname '
                      'and passport_id. Separate by space.')
        self.hotel.new_client()

    def login(self):
        print('Who are you? (enter id or return):\n')
        cl = {}
        for c in enumerate(self.hotel.clientbase):
            print(c[1])
            cl[c.id] = c[0]
        while self.run:
            opt = input('>>> ').lower()
            if opt == 'return':
                break
            if opt in cl:
                self.current_user = self.hotel.clientbase[cl[opt]]
                self.stage = 'logged'

    def isroomed(self):
        pass