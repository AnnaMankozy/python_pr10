import csv
import matplotlib.pyplot as plt

filename = "data.csv"

years = ['2015','2016','2017','2018','2019','2020','2021','2022','2023','2024']
data = {}

with open(filename, "r", encoding="utf-8-sig", newline='') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        country = row[0].strip()
        values = list(map(int, row[4:]))
        data[country] = values

print("Доступные страны:", list(data.keys()))

user_country = input("Введите страну: ").strip()

if user_country not in data:
    print("Такой страны нет!")
else:
    values = data[user_country]

    plt.bar(years, values)

    plt.xticks(years)

    plt.xlabel("Год")
    plt.ylabel("Значение показателя")
    plt.title(f"Показатель по стране: {user_country}")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()



