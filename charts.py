import matplotlib
matplotlib.use("Agg")
import pandas as pd, matplotlib.pyplot as plt

cat = pd.read_csv("cat.csv")
city = pd.read_csv("city.csv")
monthly = pd.read_csv("monthly.csv")

fig, ax = plt.subplots(1, 3, figsize=(18, 5))
ax[0].bar(cat["category"], cat["total"]); ax[0].set_title("Revenue by Category")
ax[1].bar(city["city"], city["total"]); ax[1].set_title("Revenue by City")
ax[2].plot(monthly["month"], monthly["total"], marker="o"); ax[2].set_title("Monthly Trend")
plt.tight_layout()
plt.savefig("dashboard.png")
print("dashboard.png saved")
