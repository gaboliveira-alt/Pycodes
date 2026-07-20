# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

import calendar

print(calendar.calendar(2023))
print(calendar.month(2023, 11))
first_number_day, last_day = calendar.monthrange(2023, 12)
print(list(enumerate(calendar.day_name)))
print(calendar.day_name[first_number_day])
print(calendar.day_name[calendar.weekday(2023, 12, last_day)])

for week in calendar.monthcalendar(2023, 12):
    for day in week:
        if day == 0:
            continue
        print(day)
