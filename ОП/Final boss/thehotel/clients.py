class Client:

    def __init__(self, id, name, surname, lastname, passp, comment=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.lastname = lastname
        self.passp = passp
        self.comment = comment

    def __str__(self):
        return f'[ID: {self.id}] - {self.name} {self.surname} {self.lastname}. Identity: {self.passp}. Comment: "{self.comment}"'

    def identity(self):
        return (self.id, self.name, self.surname, self.lastname, self.passp, self.comment)

    def wfriendly(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'lastname': self.lastname,
            'passp': self.passp,
            'comment': self.comment,
        }


class Roomer:

    def __init__(self, info, room, moved_in, moving_out):
        self.clientInfo = info
        self.room = room
        self.moved_in = moved_in
        self.moving_out = moving_out

    def __str__(self):
        return {
            'info': self.clientInfo.id,
            'num': self.room.number,
            'moved_in': self.moved_in,
            'moving_out': self.moving_out,
        }

    def nnn(self):
        return {
            'info': self.clientInfo.id,
            'num': self.room.number,
            'moved_in': self.moved_in,
            'moving_out': self.moving_out,
        }

    def info(self):
        a = f'Hey, {self.clientInfo.name}! Welcome back!\n'\
            f'You are living in a room number {self.room.number}, which is:\n'\
            f'1. {self.room.comfort} quality.\n2. Can fit upto {self.room.capacity} people.\n'\
            f'3. Always waiting for you to come back\n'\
            f'You have moved in on {self.moved_in}.\n'\
            f'You will not be welcomed here after {self.moving_out}\n'\
            f'Thank you for using vHotel!'
        return a