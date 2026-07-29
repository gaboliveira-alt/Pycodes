import locale
import string
from datetime import datetime
from pathlib import Path

PATH_FILE = Path(__file__).parent / "lesson180.txt"

locale.setlocale(locale.LC_ALL, "")


def brl_converting(money: float) -> str:
    return "R$".join(locale.currency(money, symbol=False, grouping=True))


data_example = datetime(2026, 7, 29)
data_person = {
    "name": "Gabriel Pinto",
    "money_value": brl_converting(1_234_456),
    "data": data_example.strftime("%d/%m/%Y"),
    "company": "Receba Enterprise",
    "phone_number": "+55 (11) 7890-5432"
}


class MyTemplate(string.Template):
    delimiter = "%"


with open(PATH_FILE) as file_person:
    text_template = file_person.read()
    template_file = MyTemplate(text_template)
    print(template_file.substitute(data_person))
