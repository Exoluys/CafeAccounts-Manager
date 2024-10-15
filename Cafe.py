import pandas as pd

# Importing DataSet
df = pd.read_csv("cafe_orders_month.csv")
total_price = df["Total Price"]

# Average of Total price
avg = total_price.mean()
print(f"{'='*40}\nStatistics Overview\n{'='*40}")
print(f"Average Total Price: ${avg:.2f}")

# Maximum price
max_price = total_price.max()
print(f"Maximum Price Paid: ${max_price:.2f}")

# Minimum price
min_price = total_price.min()
print(f"Minimum Price Paid: ${min_price:.2f}")
print("\n")

# Total spending by customer
total_spending = df.groupby('Customer Name')['Total Price'].sum().reset_index()
print(f"{'='*40}\nTotal Spending by Customers\n{'='*40}")
print(total_spending.to_string(index=False))
print("\n")

# Maximum spender
max_spender = total_spending.loc[total_spending['Total Price'].idxmax()]
print(f"{'='*40}\nMaximum Spender\n{'='*40}")
print(f"Customer Name: {max_spender['Customer Name']}")
print(f"Total Amount Spent: ${max_spender['Total Price']:.2f}\n")

# Minimum spender
min_spender = total_spending.loc[total_spending['Total Price'].idxmin()]
print(f"{'='*40}\nMinimum Spender\n{'='*40}")
print(f"Customer Name: {min_spender['Customer Name']}")
print(f"Total Amount Spent: ${min_spender['Total Price']:.2f}\n")

# Most used payment methods
payment_counts = df['Payment Method'].value_counts()
most_common_payment = payment_counts.idxmax()
print(f"{'='*40}\nMost Used Payment Method\n{'='*40}")
print(f"Payment Method: {most_common_payment}")
print(f"Total Transactions: {payment_counts.max()}")  # Optional: Display the number of transactions
print(f"{'='*40}")
