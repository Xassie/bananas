class Client:

    def __init__(self, id, name, surname, lastname, passp, comment=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.lastname = lastname
        self.passp = passp
        self.comment = comment

    def __str__(self):
        return f'{self.name} {self.surname} {self.lastname}. Identity: {self.data}. Comment: "{self.comment}""'

    def identity(self):
        return (self.name, self.surname, self.lastname, self.passp)


class Roomer:
    
    def __init__(self, info, num, moved_in, moving_out, notes=None):
        self.clientInfo = info
        self.room = num
        self.moved_in = moved_in
        self.moving_out = moving_out
        self.notes = notes