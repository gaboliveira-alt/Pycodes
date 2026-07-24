
import csv
from pathlib import Path

PATH_CSV_FILE = Path(__file__).parent / "lesson177.csv"

clients_list: list[dict[str, str]] = [
    {"Nome": "Fabricio Fontes", "Endereco": "Av 1, 22"},
    {"Nome": "Fontes Neto", "Endereco": "Av 2, 34"},
    {"Nome": "Gabriel Pinto", "Endereco": "Av 4, 98"}
]

with open(PATH_CSV_FILE, "w") as file_csv:
    collums_name = clients_list[0].keys()

    writer_csv = csv.DictWriter(file_csv, fieldnames=collums_name)
    writer_csv.writeheader()


    for client in clients_list:
        print(client)
        writer_csv.writerow(client)
