import pandas as pd, numpy as np
n = 500000
df = pd.DataFrame({
    "order_id": range(n),
    "category": np.random.choice(["Electronics","Clothes","Grocery","Books","Toys"], n),
    "city": np.random.choice(["Hyderabad","Mumbai","Delhi","Chennai","Pune"], n),
    "quantity": np.random.randint(1, 10, n),
    "price": np.random.randint(100, 5000, n),
    "date": pd.date_range("2025-01-01", periods=n, freq="min").astype(str)
})
df.to_csv("sales.csv", index=False)
print("sales.csv ready")
