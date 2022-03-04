class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x +1
        print("So far Gabigolmes", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

y = list()
print(type(y))
print(dir(y))
