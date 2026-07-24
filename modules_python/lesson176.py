import csv
from pathlib import Path

PATH_CSV_FILE = Path(__file__).parent / "lesson176.csv"


with open(PATH_CSV_FILE) as file_csv:
    read_file = csv.DictReader(file_csv)


    for line in read_file:
        print(line["Nome"], line["Idade"], line["Endereço"])


with open(PATH_CSV_FILE) as file_csv:
    read_file = csv.reader(file_csv)


    for line in read_file:
        print(line)
