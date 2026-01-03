# CodeAlpha Stock Portfolio Tracker
# Clean version without global exception handling

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))
print("-" * 40)

# Input number of stocks (assumes correct input)
num_stocks = int(input("How many different stocks do you want to buy? : "))

for i in range(num_stocks):
    stock_name = input(f"\nEnter stock name #{i+1}: ").upper()

    if stock_name not in stock_prices:
        print("❌ Stock not available. Skipping...")
        continue

    quantity = int(input(f"Enter quantity for {stock_name}: "))

    if quantity <= 0:
        print("❌ Quantity must be greater than 0. Skipping...")
        continue

    price = stock_prices[stock_name]
    value = price * quantity

    portfolio[stock_name] = {
        "price": price,
        "quantity": quantity,
        "value": value
    }

    total_investment += value

print("\n📊 Portfolio Summary")
print("-" * 40)

for stock, details in portfolio.items():
    print(
        f"{stock} | Price: ₹{details['price']} | "
        f"Quantity: {details['quantity']} | "
        f"Value: ₹{details['value']}"
    )

print("-" * 40)
print(f"💰 Total Investment Value: ₹{total_investment}")

with open("portfolio.txt", "w", encoding="utf-8") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-" * 40 + "\n")

    for stock, details in portfolio.items():
        file.write(
            f"{stock} | Price: {details['price']} | "
            f"Quantity: {details['quantity']} | "
            f"Value: {details['value']}\n"
        )

    file.write("-" * 40 + "\n")
    file.write(f"Total Investment Value: {total_investment}")

