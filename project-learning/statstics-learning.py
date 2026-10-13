import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

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


# 3. Average order value
print('Average order value', df['revenue'].mean())

monthly = df.groupby('month')['revenue'].sum()
print('Kaunsa mahina slow tha', monthly.idxmin())

# 4. agg() se ek saath kai calculations (per product: total revenue, avg order value,
# total units, aur kitne orders) -- har column ke liye alag function bhi de sakte hain
product_summary = df.groupby('product').agg(
    total_revenue=('revenue', 'sum'),
    avg_order_value=('revenue', 'mean'),
    total_units=('quantity', 'sum'),
    orders=('order_id', 'count'),
)
# print('\nProduct-wise summary (agg)')
# print(product_summary.sort_values('total_revenue', ascending=False))

#5. 3-mahine ka rolling average -- trend saaf dikhne ke liye (noise/spike smooth ho jaata hai)
monthly_df = monthly.to_frame(name='revenue')
monthly_df['rolling_3m_avg'] = monthly_df['revenue'].rolling(window=3).mean()
print('\nMonthly revenue vs 3-month rolling average')
print(monthly_df)
# NOTE: pehle 2 mahine NaN honge kyunki rolling(3) ko kam se kam 3 data points chahiye

monthly_df.index = monthly_df.index.astype(str)  # Period index ko plot ke liye string bana diya
monthly_df.plot(title='Monthly revenue vs 3-month rolling average')
plt.tight_layout()
plt.show()   # script (.py) mein chart dikhane ke liye ye line zaroori hai