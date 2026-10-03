# Import libraries
import yfinance as yf
import matplotlib.pyplot as plt

# Download a year of Apple stock data
df = yf.download("AAPL", period="1y")

# Display basic information about the dataset
print(df.head())
print(df.shape)
print(df.columns)
print(df["Close"]["AAPL"])
print(df.describe())

# Calculate the daily percent return using Apple's closing prices
df["Daily Return"] = df["Close"]["AAPL"].pct_change()

average_return = df["Daily Return"].mean()

print(f"Average Daily Return: {average_return:.2%}")

best_return = df["Daily Return"].max()

print(f"Best Daily Return: {best_return:.2%}")

worst_return = df["Daily Return"].min()

print(f"Worst Daily Return: {worst_return:.2%}")

best_day = df["Daily Return"].idxmax()

print("Best Day:", best_day)

worst_day = df["Daily Return"].idxmin()

print("Worst Day:", worst_day)

print(df.head())

# Save the raw data as a CSV file
df.to_csv("aapl_prices.csv")

# Create a line chart of Apple's closing price
plt.figure(figsize=(10,5))
plt.plot(df["Close"]["AAPL"])

# Add chart title and axis labels
plt.title("Apple Closing Price (Past Year)")
plt.xlabel("Trading Day")
plt.ylabel("Price (USD)")

# Save the chart as a PNG file and display it
plt.tight_layout()
plt.savefig("aapl_price.png")
plt.show()