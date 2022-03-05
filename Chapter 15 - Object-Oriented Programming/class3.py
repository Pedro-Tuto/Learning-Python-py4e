class Gabigolmes:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, 'construído')

    def party(self):
        self.x = self.x + 1
        print(self.name,'contagem:', self.x)
    
s = Gabigolmes("Eto")
s.party()

j = Gabigolmes("Atalaia")
j.party()
s.party()
