class PartyAnimal:
    x = 0
    def _init_(self):
        print('Classe construída')

    def party(self):
        self.x = self.x + 1
        print('Até agora', self.x)
    
    def _del_(self):
        print('Classe destruída', self.x)

an = PartyAnimal()
an._init_()
an.party()
an.party()
an = 42
print('an contem', an)

