class Musician :
    def __init__(self,members):
        self.members=members
    def __str__ (self):
        print("------------")

    def __repr__(self):
        print("------------")

    def get_instrument(self):
        return "method that returns string."

    def play_solo(self):
        return "method that returns string."



class Band(Musician) :
    def __init__(self,name,members):
        self.name = name 
        super().__init__(members)

    def play_solos(self):
        print("method <>-play a solo")

        
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__ (self):
        print("-----------")

    @classmethod
    def to_list(cls):
        print(cls.members)


class Guitarist(Band) :
    def __init__(self,name,members):
        self.name = name 
        super().__init__(name)

    def get_instrument():
        return "guitar"

    def play_solos(self):
        print("face melting guitar solo")

class Bassist(Band) :
    def __init__(self,name,members):
        self.name = name 
        super().__init__(name)

    def get_instrument():
        return "bass"
    def play_solos(self):
        print("bom bom buh bom")

class Drummer(Band) :
    def __init__(self,name,members):
        self.name = name 
        super().__init__(name)

    def get_instrument():
        return "drums"
    def play_solos(self):
        print("rattle boom crash")

