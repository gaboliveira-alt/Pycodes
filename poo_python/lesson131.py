
class Pen:
    def __init__(self, color_pen):
        self.color_pen = color_pen
    
    @property
    def color(self):
        print('Voce pegou a cor')
        return self.color_pen
    
    @property
    def pen_top_color(self):
        return 'cor da tampa do bagulho da caneta'
    

pen_01 = Pen('Vermelho')
print(pen_01.color)
print(pen_01.pen_top_color)