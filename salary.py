import json
import csv
import os

data = {
    "Имя": "Иван",
    "Возраст": 25,
    "Город": "Москва"
}

with open("salary.json", "w", encoding = "UTF-8") as file:
    json.dump(data, file, ensure_ascii = False, indent = 4)

with open("salary.json", "r", encoding = "UTF-8") as file:
    data = json.load(file)

rows = [
    data["Имя"],
    data["Возраст"],
    data["Город"],
    "Стажёр",
    50000
]

headers = ["Имя", "Возраст", "Город", "Должность", "Зарплата"]

with open("salary.csv", "a", encoding="UTF-8", newline="") as file:
    writer = csv.writer(file)

    if not os.path.exists("salary.csv"):
        writer.writerow(headers)

    writer.writerow(rows)