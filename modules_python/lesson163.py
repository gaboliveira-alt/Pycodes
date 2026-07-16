from datetime import datetime

data_example = datetime.strptime("2026-12-13 07:23:54", "%Y-%m-%d %H:%M:%S")
print(data_example.strftime("%d/%m/%Y"))
print(data_example.strftime("%d/%m/%Y %H:%M"))
print(data_example.strftime("%d/%m/%Y %H:%M:%S"))
print(data_example.strftime("%Y"), data_example.year)
print(data_example.strftime("%d"), data_example.day)
print(data_example.strftime("%m"), data_example.month)
print(data_example.strftime("%H"), data_example.hour)
print(data_example.strftime("%M"), data_example.minute)
print(data_example.strftime("%S"), data_example.second)
