import csv
import matplotlib.pyplot as plt

filename = "laba9.csv"
data = {}

with open(filename, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        if not row or len(row) < 5:
            continue
        row = [x.replace('"', '').strip() for x in row]
        country = row[4]

        values = []
        for v in row:
            try:
                val = float(v.replace(",", "."))
                values.append(val if val > 0 else 0)
            except:
                pass

        data[country] = values[-10:] 

countries_to_plot = ["USA", "UKR"]
values_to_plot = [sum(data[c]) for c in countries_to_plot]

fig, ax = plt.subplots(figsize=(7,7), subplot_kw=dict(aspect="equal"))

def func(pct, allvals):
    absolute = pct/100.*sum(allvals)
    return f"{pct:.1f}%\n({absolute:.10f})"

wedges, texts, autotexts = ax.pie(
    values_to_plot,
    autopct=lambda pct: func(pct, values_to_plot),
    startangle=90,
    textprops=dict(color="w"))

ax.legend(
    wedges,
    countries_to_plot,
    title="Країни",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=10, weight="bold")
ax.set_title("Сумарна інфляція США та України (2015-2024)")

plt.show()

