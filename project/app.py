from finance import get_stock
from charts import create_chart
from ai import analyze


def stock(ticker: str):

    data = get_stock(ticker)

    chart = create_chart(data["history"])

    report = analyze(
        data["name"],
        data["price"],
        data["pe"],
        data["market_cap"],
        data["dividend"]
    )

    return {
        "company": data["name"],
        "price": data["price"],
        "market_cap": data["market_cap"],
        "pe": data["pe"],
        "dividend": data["dividend"],
        "chart": chart,
        "analysis": report
    }


result = stock("AAPL")

print("\n=== STOCK REPORT ===")
print("Company:", result["company"])
print("Price:", result["price"])
print("Market Cap:", result["market_cap"])
print("P/E:", result["pe"])
print("Dividend:", result["dividend"])
print("\nAnalysis:\n", result["analysis"])
