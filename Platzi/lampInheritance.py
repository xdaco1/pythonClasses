from lamp import Lamp

class WallLamp(Lamp):
    def getStatus(self):
        return self._is_turned_on

if __name__ == "__main__":    
    wlamp = WallLamp(is_turned_on=True)
    print('Is The wall lamp turned on?: {}'.format(wlamp.getStatus()))