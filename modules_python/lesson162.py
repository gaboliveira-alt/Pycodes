from datetime import datetime

date_str_data: str = "2026/06/22 15:08:23"
date_str_data: str = "22/06/2026"
date_str_fmt: str = "%d/%m/%Y"

data = datetime.strptime(date_str_data, date_str_fmt)
print(data)
