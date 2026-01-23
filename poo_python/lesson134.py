
class Writer:
    def __init__(self, name):
        self.name = name
        self._tool = None
    
    @property
    def tool(self):
        return self._tool
    
    @tool.setter
    def tool(self, type_tool):
        self._tool = type_tool


class Tool:
    def __init__(self, name):
        self._name = name
    
    def to_write(self):
        print(f'{self._name} está escrevendo um livro bla bla')


writer_example = Writer('Michael Cricton')
pen_example = Tool('Caneta Esferografica')
type_writer = Tool('Maquina de Escrever')
writer_example.tool = type_writer

pen_example.to_write()
type_writer.to_write()
writer_example.tool.to_write()