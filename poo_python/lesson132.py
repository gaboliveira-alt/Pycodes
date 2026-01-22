class Pen:
    def __init__(self, color):
        self.color = color
        self._top_color = None
    
    @property
    def color(self):
        print('ESTOU NO GETTER')
        return self._color
    
    @color.setter
    def color(self, value):
        print('ESTOU NO SETTER')
        if value == 'Rosa' or value == 'Pink':
            raise ValueError('Não aceito essa cor aqui não!')
        self._color = value
    
    @property
    def top_color(self):
        return self._top_color
    
    @top_color.setter
    def top_color(self, value):
        self._top_color = value
        
    
    
pen_01 = Pen('Roxo')
pen_01.color = 'Azul'
print(pen_01.color)