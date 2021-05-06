class Band:
    def __init__(self,name,members):
        self.name = name
        self.members = members
        Band.instances.append(self)
    
    def play_solos(self):
        message=[]
        for i in self.members:
            string_message=str(i).split()[len(str(i).split())-1::]
            # print(string_message[0])
            if string_message[0] == 'guitar':
                message.append('face melting guitar solo')
            if string_message[0] == 'bass':
                message.append('bom bom buh bom')
            if string_message[0] == 'drums':
                message.append('rattle boom crash')
        return message
            
    @classmethod
    def to_list(cls):
        return cls.instances


class Musician():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def get_instrument(self):
        return f"{self.instrument}"

    def play_solo(self):
        return f"{self.solo_play}"



class Guitarist(Musician):
    instrument = 'guitar'
    def __init__(self, name):
        super().__init__(name)
        self.solo_play = 'face melting guitar solo'



class Bassist(Musician):
    instrument = 'bass'
    def __init__(self, name):
        super().__init__(name)
        self.solo_play = 'bom bom buh bom'


class Drummer(Musician):
    instrument = 'drums'
    def __init__(self, name):
        super().__init__(name)
        self.solo_play = 'rattle boom crash'

ob1=Drummer("Mohammad")
print(ob1.__str__())
print(ob1.__repr__())

ob2=Bassist("Mohammad")
print(ob2.__str__())
print(ob2.__repr__())

# print(ob1.__str__())
# print(ob1.__str__())
# print(ob1.__str__())