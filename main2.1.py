import csv
import matplotlib.pyplot as plt

filename = "data.csv"

years = ['2015','2016','2017','2018','2019','2020','2021','2022','2023','2024']
data = {}

with open(filename, "r", encoding="utf-8-sig", newline='') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        country = row[0].strip()
        values = list(map(int, [v.strip() for v in row[4:]]))
        data[country] = values

print("Countries loaded:", list(data.keys()))

if "Spain" in data and "Mexico" in data:
    plt.plot(years, data["Spain"], label="Spain", linewidth=3)
    plt.plot(years, data["Mexico"], label="Mexico", linewidth=3)

    plt.title("Young people newly infected with HIV")
    plt.xlabel("Year")
    plt.ylabel("Indicator value")
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("Не знайдено одну з країн!")
    print("Є такі країни:", list(data.keys()))
