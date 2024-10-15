import pandas as pd

# Importing DataSet
df = pd.read_csv("cafe_orders_month.csv")
total_price = df["Total Price"]  # Extracting the 'Total Price' column for analysis

# Average of Total price
avg = total_price.mean() # Calculating the average total price
print(f"{'='*40}\nStatistics Overview\n{'='*40}")
print(f"Average Total Price: ${avg:.2f}") # Displaying the average with two decimal places

# Maximum price
max_price = total_price.max() # Finding the maximum price paid
print(f"Maximum Price Paid: ${max_price:.2f}") # Displaying the maximum price

# Minimum price
min_price = total_price.min() # Finding the minimum price paid
print(f"Minimum Price Paid: ${min_price:.2f}\n") # Displaying the minimum price

# Total spending by customer
total_spending = df.groupby('Customer Name')['Total Price'].sum().reset_index() # Grouping by customer and summing their total spending
print(f"{'='*40}\nTotal Spending by Customers\n{'='*40}")
print(f'{total_spending.to_string(index=False)}\n') # Printing the total spending table without row indices

# Maximum spender
max_spender = total_spending.loc[total_spending['Total Price'].idxmax()] # Identifying the customer with the maximum total spending
print(f"{'='*40}\nMaximum Spender\n{'='*40}")
print(f"Customer Name: {max_spender['Customer Name']}") # Displaying the name of the maximum spender
print(f"Total Amount Spent: ${max_spender['Total Price']:.2f}\n") # Displaying the total amount spent by the maximum spender

# Minimum spender
min_spender = total_spending.loc[total_spending['Total Price'].idxmin()] # Identifying the customer with the minimum total spending
print(f"{'='*40}\nMinimum Spender\n{'='*40}")
print(f"Customer Name: {min_spender['Customer Name']}") # Displaying the name of the minimum spender
print(f"Total Amount Spent: ${min_spender['Total Price']:.2f}\n") # Displaying the total amount spent by the minimum spender

# Most used payment methods
payment_counts = df['Payment Method'].value_counts() # Counting occurrences of each payment method
most_common_payment = payment_counts.idxmax() # Identifying the most common payment method
print(f"{'='*40}\nMost Used Payment Method\n{'='*40}")
print(f"Payment Method: {most_common_payment}") # Displaying the most used payment method
print(f"Total Transactions: {payment_counts.max()}")   # Displaying the number of transactions for the most common payment method
print(f"{'='*40}") # Final line for visual separation
