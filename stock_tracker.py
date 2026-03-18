# Stock Portfolio Tracker

# Hardcoded stock prices (you can change/add more)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 300,
    "AMZN": 3300
}

portfolio = {}
total_investment = 0

print("📊 Welcome to Stock Portfolio Tracker")

# Taking user input
while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        portfolio[stock_name] = quantity
    else:
        print("❌ Stock not available in price list!")

# Calculating total investment
print("\n📈 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock} - Quantity: {qty}, Price: {price}, Value: {value}")

print(f"\n💰 Total Investment Value: {total_investment}")

# Optional: Save to file
save = input("\nDo you want to save result to file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock} - Qty: {qty}, Price: {price}, Value: {value}\n")
        file.write(f"\nTotal Investment: {total_investment}")
    
    print("✅ Data saved to portfolio.txt")
