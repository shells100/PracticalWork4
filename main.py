import csv

header = ["Животное", "Среда обитания"]
rows = [
    ["Медведь", "Лес"],
    ["Дельфин", "Океан"],
    ["Верблюд", "Пустыня"]
    ]

with open("animals.csv", "w", encoding = "UTF-8", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

with open ("animals.csv", "r", encoding = "UTF-8", newline = "") as file_read:
    reader = csv.reader(file_read)
    for row in reader:
        if row[1] == "Лес":
            print(row[0])