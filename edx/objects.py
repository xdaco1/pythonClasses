# https://books.trinket.io/pfe/14-objects.html
class PartyAnimal:
    x = 0
    name=''
    def __init__(self,nam):
        self.name = nam
        print('I\'m constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

    def __del__(self):
        print('I\'m destructed')

# an = PartyAnimal()
# an.party()
# an.party()
# print('an is type {} and contains {}'.format(type(an),an))
# an = 42
# print('an is type {} and contains {}'.format(type(an),an))

s = PartyAnimal('Sally')
s.party()
j = PartyAnimal('Jim')
j.party()
s.party()