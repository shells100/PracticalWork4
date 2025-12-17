import csv

header = ["Имя", "Возраст", "Город", "Должность"]
rows = [
    ["Алексей", 23, "Москва", "Разработчик"],
    ["Дмитрий", 31, "Санкт-Петербург", "Заместитель"],
    ["Денис", 49, "Москва", "Директор"],
    ["Иван", 29, "Москва", "Инженер"]
    ]

with open("csv_file.csv", "w", encoding = "UTF-8") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

with open ("csv_file.csv", "r", encoding = "UTF-8") as file_read:
    reader = csv.reader(file_read)
    next(reader)
    
    for row in reader:
        if int(row[1]) > 30:
            print(row[0])