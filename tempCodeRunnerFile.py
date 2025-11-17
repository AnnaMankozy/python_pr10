import csv
import matplotlib.pyplot as plt

FILENAME = "data.csv"

# Завантажуємо дані з CSV
countries = {}

with open(FILENAME, "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        if len(row) >= 14:  # 4 колонки + 10 значень
            country_name = row[0]
            values = list(map(int, row[4:14]))  # беремо 10 значень
            countries[country_name] = values

# Виводимо список країн
print("Доступні країни:", list(countries.keys()))

user_country = input("Введіть назву країни: ")

if user_country not in countries:
    print("❌ Такої країни немає у файлі!")
else:
    data = countries[user_country]
    years = list(range(2015, 2025))
    plt.bar(years, data)
    plt.xlabel("Рік")
    plt.ylabel("Значення показника")
    plt.title(f"Показник для країни: {user_country}")
    plt.grid(axis="y")
    plt.show()