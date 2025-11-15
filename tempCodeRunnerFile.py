import csv
import matplotlib.pyplot as plt

filename = "data.csv"

countries = []
years = []
data = {}

with open(filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)

    years = header[4:]

    for row in reader:
        country = row[0]
        countries.append(country)
        values = list(map(int, row[4:]))
        data[country] = values

plt.plot(years, data["Spain"], label="Spain", linewidth=3)
plt.plot(years, data["Mexico"], label="Mexico", linewidth=3)

plt.title("Young people newly infected with HIV")
plt.xlabel("Year")
plt.ylabel("Indicator value")

plt.legend()
plt.grid(True)
plt.show()

user_country = input("Enter country name (Spain/Mexico): ")

if user_country in data:
    plt.bar(years, data[user_country])
    plt.title(f"Indicator for {user_country}")
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()
else:
    print("Country not found in file.")