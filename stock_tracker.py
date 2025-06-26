import csv
from datetime import datetime

class StockPortfolioTracker:
    def __init__(self):
        self.stock_prices = {
            "AAPL": 180.00,
            "TSLA": 250.00,
            "GOOGL": 140.00,
            "MSFT": 415.00,
            "AMZN": 155.00
        }
        self.portfolio = {}

    def display_available_stocks(self):
        print("\nAvailable Stocks and Prices:")
        for symbol, price in self.stock_prices.items():
            print(f"{symbol}: ${price:.2f}")

    def input_portfolio(self):
        self.display_available_stocks()
        while True:
            symbol = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
            if symbol == 'DONE':
                break
            if symbol not in self.stock_prices:
                print("Invalid stock symbol.")
                continue
            try:
                quantity = int(input(f"Enter quantity for {symbol}: "))
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
                self.portfolio[symbol] = self.portfolio.get(symbol, 0) + quantity
            except ValueError:
                print("Please enter a valid number.")

    def calculate_total_value(self):
        print("\nYour Portfolio Summary:")
        total = 0
        for symbol, quantity in self.portfolio.items():
            price = self.stock_prices[symbol]
            value = price * quantity
            total += value
            print(f"{symbol}: {quantity} shares @ ${price:.2f} = ${value:.2f}")
        print(f"\nTotal Investment Value: ${total:.2f}")
        return total

    def save_to_txt(self, total):
        filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write("Stock Portfolio\n")
            for symbol, quantity in self.portfolio.items():
                price = self.stock_prices[symbol]
                value = price * quantity
                f.write(f"{symbol}: {quantity} shares @ ${price:.2f} = ${value:.2f}\n")
            f.write(f"\nTotal Investment: ${total:.2f}\n")
        print(f"Saved to {filename}")

    def save_to_csv(self, total):
        filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Stock', 'Quantity', 'Price', 'Value'])
            for symbol, quantity in self.portfolio.items():
                price = self.stock_prices[symbol]
                value = price * quantity
                writer.writerow([symbol, quantity, price, value])
            writer.writerow(['', '', 'Total', total])
        print(f"Saved to {filename}")

    def run(self):
        print("=== Stock Portfolio Tracker ===")
        self.input_portfolio()
        total = self.calculate_total_value()

        save_choice = input("Save results to file? (txt/csv/none): ").strip().lower()
        if save_choice == 'txt':
            self.save_to_txt(total)
        elif save_choice == 'csv':
            self.save_to_csv(total)
        else:
            print("Results not saved.")

# Run the simplified tracker
if __name__ == "__main__":
    tracker = StockPortfolioTracker()
    tracker.run()
