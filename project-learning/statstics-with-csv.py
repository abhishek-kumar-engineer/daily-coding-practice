import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'sales.csv')
df = pd.read_csv(DATA_PATH, parse_dates=['date'])
df['month'] = df['date'].dt.to_period('M')

# print(df.head())

# 1. Kaunsa product sabse zyada bika (units) 
print('Kaunsa product sabse zyada bika (units) ')
print(df.groupby('product')['quantity'].sum().sort_values(ascending=False))

# aur kisne sabse zyada kamaya (revenue)
print('kisne sabse zyada kamaya (revenue)')
print(df.groupby('product')['revenue'].sum().sort_values(ascending=False))

# 2. Kaunsa mahina slow tha
monthly = df.groupby('month')['revenue'].sum()
print('Kaunsa mahina slow tha', monthly.idxmin())

monthly.plot(kind='bar', title='Monthly revenue')
plt.tight_layout()
plt.show()   # script (.py) mein chart dikhane ke liye ye line zaroori hai


# 3. Average order value
print('Average order value', df['revenue'].mean())
