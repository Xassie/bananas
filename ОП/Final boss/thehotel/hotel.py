import datetime
from thehotel.clients import *


class Hotel:
    
    def __init__(self):
        self.rooms = []
        self.clientbase = []
        self.clients_init()
        self.rooms_init()
        self.check_roomers
    
    def rooms_init(self):
        import csv
        with open('.\\data\\rooms.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for line in reader:
                self.rooms.append(Room(**dict(line)))

    def rooms_rewrite(self):
        pass

    
    def clients_init(self):
        import csv
        with open('.\\data\\clientbase.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for line in reader:
                self.clientbase.append(Client(**dict(line)))


    def clients_append(self):
        pass

    
    def new_client(self):
        while True:
            dat = input('Please enter your Name, Surname, Lastname '
                      'and passport_id. Separate by space\n>>> ')
            dat = dat.split(' ')
            if len(dat) != 4:
                continue
            comm = input("if you'd like to add a comment - this is a good time for it\n>>> ")
            break
        self.clientbase.append(Client(len(self.clientbase+2, *dat, comm)))
        self.clients_append()
        
        


    def new_roomer(self):
        pass

    
    def exp_roomer(self):
        pass


    def check_roomers(self):
        pass

    
    def movein(self):
        pass

        

class Room:
    
    def __init__(self, number, capacity, comfort, cost, busy):
        self.number = int(number)
        self.capacity = int(capacity)
        self.comfort = comfort
        self.cost = float(cost)
        self.busy = bool(busy)

    def __str__(self):
        return f'Room #{self.number} for {self.capacity} ppl. Quality={self.comfort} for {self.cost} rub. Busy: {self.busy}'
