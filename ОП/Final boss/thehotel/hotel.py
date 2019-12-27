import datetime
from thehotel.clients import *
from csv import DictReader, DictWriter


class Hotel:
    
    def __init__(self):
        self.rooms = []
        self.roomers = []
        self.clientbase = []
        self.clients_init()
        self.rooms_init()
        self.roomers_init()
        self.check_roomers()
    
    def rooms_init(self):
        with open('.\\data\\rooms.csv', 'r') as file:
            reader = DictReader(file, delimiter=';')
            for line in reader:
                self.rooms.append(Room(**dict(line)))

    def rooms_rewrite(self):
        names = []
        for i in self.rooms[0]:
            names.append(i)
        with open('.\\data\\rooms.csv', 'w') as file:
            writer = DictWriter(file, fieldnames=names, delimiter=';')
            writer.writeheader()
            writer.writerows(self.rooms)


    def roomers_init(self):
        with open('.\\data\\roomers.csv', 'r') as file:
            reader = DictReader(file, delimiter=';')
            for line in reader:
                self.roomers.append(Roomer(**dict(line)))

    
    def clients_init(self):
        with open('.\\data\\clientbase.csv', 'r') as file:
            reader = DictReader(file, delimiter=';')
            for line in reader:
                self.clientbase.append(Client(**dict(line)))


    def clients_append(self, client):
        name = []
        for i in client:
            name.append(i)
        with open('.\\data\\roomers.csv', 'a') as file:
            writer = DictWriter(file, fieldnames=name, delimiter=';')
            writer.writerows(client)

    
    def new_client(self):
        while True:
            dat = input('>>> ')
            if dat.lower == 'return':
                break
            dat = dat.split(' ')
            if len(dat) != 4:
                continue
            comm = input("if you'd like to add a comment - this is a good time for it\n>>> ")
            self.clientbase.append(Client(*[len(self.clientbase)+2, *dat, comm]))
            self.clients_append(self.clientbase[-1].wfriendly())
            break

    
    def rewrite_roomers(self):
        names = []
        for i in self.roomers[0]:
            names.append(i)
        with open('.\\data\\roomers.csv', 'w') as file:
            writer = DictWriter(file, fieldnames=names, delimiter=';')
            writer.writeheader()
            writer.writerows(self.roomers)


    def check_roomers(self):
        a = datetime.datetime.now()
        a = datetime.date(a.year, a.month, a.day)
        for i in enumerate(self.roomers):
            if datetime.date(i[1].moving_out.split('/')) < a:
                self.roomers.pop(i[0])
        self.rewrite_roomers()
    
    def movein(self, client, num, moving_out, notes=''):
        a = datetime.datetime.now()
        self.roomers.append(Roomer(*client.info, num, f'{a.year}/{a.month}/{a.day}', moving_out, notes))
        self.rewrite_roomers()
        


class Room:
    
    def __init__(self, number, capacity, comfort, cost, busy):
        self.number = int(number)
        self.capacity = int(capacity)
        self.comfort = comfort
        self.cost = float(cost)
        self.busy = bool(busy)

    def __str__(self):
        return f'Room #{self.number} for {self.capacity} ppl. Quality={self.comfort} for {self.cost} rub. Busy: {self.busy}'
