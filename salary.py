import json
import csv
import os

json_data = {
    "Имя": "Иван",
    "Возраст": 25,
    "Город": "Москва"
}

with open("test_json.json", "w", encoding = "UTF-8") as file:
    json.dump(json_data, file, ensure_ascii = False)

with open("test_json.json", "r", encoding= "UTF-8") as file:
    data = json.load(file)

headers = ["Имя", "Возраст", "Город", "Должность", "Зарплата"]

row = [
    data["Имя"],
    data["Возраст"],
    data["Город"],
    "Стажёр",
    50000
]

if not os.path.exists("employees_with_salary.csv"):
    with open("employees_with_salary.csv", "w", encoding = "UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerow(row)
else:
    with open("employees_with_salary.csv", "a", encoding = "UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(row)