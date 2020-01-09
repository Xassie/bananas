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

    def roomers_init(self):
        with open('.\\data\\roomers.csv', 'r') as file:
            reader = DictReader(file, delimiter=';')
            for line in reader:
                self.roomers.append(Roomer(self.clientbase[int(line['info'])-1],
                                           self.rooms[int(line['num'])-1],
                                           line['moved_in'], line['moving_out']))

    
    def rewrite_rooms(self):
        name = []
        rooms = []
        for i in self.rooms:
            rooms.append(i.wfry())
        for i in rooms[0]:
            name.append(i)
        with open('.\\data\\rooms.csv', 'w') as file:
            writer = DictWriter(file, fieldnames=name, delimiter=';')
            writer.writeheader()
            writer.writerows(rooms)



    def clients_init(self):
        with open('.\\data\\clientbase.csv', 'r') as file:
            reader = DictReader(file, delimiter=';')
            for line in reader:
                self.clientbase.append(Client(**dict(line)))


    def clients_append(self, client):
        name = []
        for i in client:
            name.append(i)
        with open('.\\data\\clientbase.csv', 'a') as file:
            writer = DictWriter(file, fieldnames=name, delimiter=';')
            writer.writerow(client)
        print('done')

    
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
        if len(self.roomers):
            names = []
            people = []
            for i in self.roomers:
                people.append(i.nnn())
            for i in people[0]:
                names.append(i)
            with open('.\\data\\roomers.csv', 'w') as file:
                writer = DictWriter(file, fieldnames=names, delimiter=';')
                writer.writeheader()
                writer.writerows(people)
        else:
            with open('.\\data\\roomers.csv', 'w') as file:
                pass


    def check_roomers(self):
        if len(self.roomers):
            a = datetime.datetime.now()
            a = datetime.date(a.year, a.month, a.day)
            for i in enumerate(self.roomers):
                b = i[1].moving_out.split('/')
                b = [int(x) for x in b]
                if datetime.date(*b) < a:
                    i[1].room.busy = ''
                    self.roomers.pop(i[0])
            self.rewrite_roomers()
            self.rewrite_rooms()
    

    def expansion(self, client, exp):
        time = datetime.date(*[int(x) for x in client.moving_out.split('/')])
        time = time + datetime.timedelta(days=exp)
        client.moving_out = f'{time.year}/{time.month}/{time.day}'
        self.rewrite_roomers()

    
    def movein(self, client, room, days):
        a = datetime.datetime.now()
        b = a + datetime.timedelta(days=days)
        room.busy = True
        self.roomers.append(Roomer(client, room, f'{a.year}/{a.month}/{a.day}', f'{b.year}/{b.month}/{b.day}'))
        self.rewrite_roomers()
        self.rewrite_rooms()
        

    def kickout(self, room, client):
        room.busy = ''
        for i in enumerate(self.roomers):
            if i[1].clientInfo.id == client:
                self.roomers.pop(i[0])
                self.rewrite_rooms()
                self.rewrite_roomers()
                break



class Room:
    
    def __init__(self, number, capacity, comfort, cost, busy):
        self.number = int(number)
        self.capacity = int(capacity)
        self.comfort = comfort
        self.cost = float(cost)
        self.busy = busy

    def __str__(self):
        if self.busy:
            a = True
        else:
            a = False
        return f'Room #{self.number} for {self.capacity} ppl. Quality={self.comfort} for {self.cost} rub. Busy: {a}'

    def wfry(self):
        return {
            'number' : self.number,
            'capacity' : self.capacity,
            'comfort' : self.comfort,
            'cost' : self.cost,
            'busy' : self.busy,
        }
