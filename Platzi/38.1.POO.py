class Lamp:

    # Class variable
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    #Constructor method
    def __init__(self,is_turned_on):
        self._is_turned_on = is_turned_on # Private variable

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self): # private method
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

def run():
    lamp = Lamp(is_turned_on=True)
    
    while True:
        command = str(input('''
            ¿What do you want to do?

            [1] Turn on the light
            [2] Turn off the light
            [q]uit
            \n'''))
        
        if command == '1':
            lamp.turn_on()
        elif command == '2':
            lamp.turn_off()
        elif command == 'q':
            print('\nBye!!')
            break
        else:
            print('Try again: "{}" is not a valid option'.format(command))
            continue

if __name__ == "__main__":
    run()