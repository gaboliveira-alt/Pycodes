
class MyOpen:
    def __init__(self, path_file, file_mode):
        self.path_file = path_file
        self.file_mode = file_mode
        self._file = None
    
    def __enter__(self):
        print('ABRINDO O ARQUIVO')
        self._file = open(self.path_file, self.file_mode, encoding='utf8')
        return self._file
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO O ARQUIVO')
        if self._file is not None:
            self._file.close()
        
        # raise class_exception(*exception_.args).with_traceback(traceback_)
        
        # print(class_exception)
        # print(exception_)
        # print(traceback_)
        
        # return True - Tratei a exceção


with MyOpen('lesson149.txt', 'w') as example_file:
    example_file.write('Linha 1\n')
    example_file.write('Linha 2\n')
    example_file.write('Linha 3\n')
    print('WITH', example_file)