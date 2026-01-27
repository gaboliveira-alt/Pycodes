from math import log
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente este metodo!')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success!: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        formated_message = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a', encoding='utf-8') as log_file:
            log_file.write(formated_message)
            log_file.write('\n')
            log_file.write(formated_message)
            log_file.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    example_log = LogPrintMixin()
    example_log.log_error('aqui tem erro parça')
    example_log.log_success('aqui tem sucesso hein!')
    example_log1 = LogFileMixin()
    example_log1.log_error('Salvando no .txt')
    example_log1.log_success('Salvando no .txt')