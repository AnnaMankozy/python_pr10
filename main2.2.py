import csv
import matplotlib.pyplot as plt

filename = "data.csv"

years = ['2015','2016','2017','2018','2019','2020','2021','2022','2023','2024']
data = {}

with open(filename, "r", newline='') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        country = row[0].strip()
        try:
            values = list(map(int, row[4:]))
            data[country] = values
        except ValueError:
            continue 

print("Доступні країни:", list(data.keys()))
user_country = input("Введіть країну: ").strip()

if user_country not in data:
    print("Такої країни немає!")
else:
    values = data[user_country]

    plt.bar(years, values)

    plt.xticks(years)

    plt.xlabel("Рік")
    plt.ylabel("Значення показника")
    plt.title(f"Показник по країні: {user_country}")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()



