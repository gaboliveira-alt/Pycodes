from log import LogFileMixin, LogPrintMixin

example_log = LogPrintMixin()
example_log.log_error('aqui tem erro parça')
example_log.log_success('aqui tem sucesso hein!')
example_log1 = LogFileMixin()
example_log1.log_error('Salvando no .txt')
example_log1.log_success('Salvando no .txt')