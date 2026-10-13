import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
n = 1000
products = ['Laptop', 'Phone', 'Headphones', 'Keyboard', 'Mouse']
price = {'Laptop': 55000, 'Phone': 20000, 'Headphones': 3000, 'Keyboard': 1500, 'Mouse': 800}

df = pd.DataFrame({
    'date': pd.to_datetime('2025-01-01') + pd.to_timedelta(rng.integers(0, 365, n), unit='D'),
    'product': rng.choice(products, n, p=[0.1, 0.3, 0.2, 0.15, 0.25]),
    'quantity': rng.integers(1, 5, n),
})
df['revenue'] = df['quantity'] * df['product'].map(price)
df['month'] = df['date'].dt.to_period('M')

# 1. Kaunsa product sabse zyada bika (units) aur kisne sabse zyada kamaya (revenue)
# print(df.groupby('product')['quantity'].sum().sort_values(ascending=False))
# print(df.groupby('product')['revenue'].sum().sort_values(ascending=False))

# 2. Kaunsa mahina slow tha
monthly = df.groupby('month')['revenue'].sum()
print(monthly.idxmin())
monthly.plot(kind='bar')

# 3. Average order value
print(df['revenue'].mean())



monthly.plot(kind='bar', title='Monthly revenue')
plt.tight_layout()
plt.show()