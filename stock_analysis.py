import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("AAPL", period="1y")

print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())

df.to_csv("aapl_prices.csv")

plt.figure(figsize=(10,5))

plt.plot(df["Close"]["AAPL"])

plt.title("Apple Closing Price (Past Year)")
plt.xlabel("Trading Day")
plt.ylabel("Price (USD)")

plt.tight_layout()
plt.savefig("aapl_price.png")
plt.show()