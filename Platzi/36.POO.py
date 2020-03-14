class Car:
    __wheels__ = 4
    color = ''

    def getColor(self):
        return self.color
    
    def getwheels(self):
        return self.__wheels__
        
    def setColor(self,nColor):
        self.color = nColor

if __name__ == "__main__":        

    car1 = Car()
    car1.setColor('green')
    car2 = Car()
    car2.setColor('black')

    print('car1 has {} wheels and is {}'.format(car1.getwheels(),car1.getColor()))
    print('car2 has {} wheels and is {}'.format(car2.getwheels(),car2.getColor()))