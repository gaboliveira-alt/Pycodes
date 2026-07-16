from datetime import datetime

from pytz import timezone

date_str_data_01: str = "2026/06/22 15:08:23"
date_str_data: str = "22/06/2026"
date_str_fmt: str = "%d/%m/%Y"

data = datetime.strptime(date_str_data, date_str_fmt)
print(data)

data_01 = datetime.now()
print(data_01.timestamp())
print(data_01.fromtimestamp(1782153607.623211))

data_02 = datetime(2026, 6, 22, 15, 54, 23, tzinfo=timezone("Asia/Tokyo"))
