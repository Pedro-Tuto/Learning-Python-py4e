class Gabigolmes:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, 'construído')

    def party(self):
        self.x = self.x + 1
        print(self.name,'contagem:', self.x)

class FãDeFutebol(Gabigolmes):
    pontos = 0 
    def gol(self):
        self.pontos = self.pontos + 7
        self.party()
        print(self.name, "pontos", self.pontos)

s = Gabigolmes("Eto")
s.party()

j = FãDeFutebol("Atalaia")
j.party()
j.gol()


    