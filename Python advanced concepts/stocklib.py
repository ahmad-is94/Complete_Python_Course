from nsetools import Nse

# Initialize the NSE object
nse = Nse()

try:
    # 1. Fetch a live stock quote (example: Infosys -> 'infy')
    quote = nse.get_quote("infy")

    print("--- Stock Quote: INFY ---")
    print("Company:   ", quote.get("companyName"))
    print("Last Price:", quote.get("lastPrice"))
    print("Day High:  ", quote.get("dayHigh"))
    print("Day Low:   ", quote.get("dayLow"))

    # 2. Fetch top gainers
    print("\n--- Top 5 Gainers ---")
    top_gainers = nse.get_top_gainers()

    for stock in top_gainers[:5]:
        symbol = stock.get("symbol")
        ltp = stock.get("ltp")          # Last Traded Price
        change = stock.get("netPrice")  # Percentage change
        print(f"{symbol}: LTP = {ltp} | Change = {change}%")

except Exception as e:
    print("Error fetching NSE data:", e)