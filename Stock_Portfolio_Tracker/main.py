stocks = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 150,
    "AMAZON": 200
}

total_value = 0

print("=== MY STOCK PORTFOLIO TRACKER ===")

print("\nAvailable Companies:")
print("APPLE - Technology")
print("TESLA - Electric Cars")
print("GOOGLE - AI & Search")
print("AMAZON - Online Shopping")

while True:

    stock_name = input("\nEnter Company Name or DONE: ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:

        quantity = int(input("How many shares do you want to buy? "))

        investment = stocks[stock_name] * quantity

        total_value += investment

        print(f"You invested ${investment} in {stock_name}")

    else:
        print("Sorry! Company not available.")

print("\n=== FINAL INVESTMENT REPORT ===")
print("Total Portfolio Value:", total_value)

if total_value >= 1000:
    print("Great! Your portfolio is growing well.")

else:
    print("Keep investing to grow your portfolio.")
         