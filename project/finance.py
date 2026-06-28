import yfinance as yf


def get_stock(symbol: str):

    stock = yf.Ticker(symbol)

    info = stock.info

    hist = stock.history(period="1y")

    return {
        "name": info.get("longName"),
        "price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "pe": info.get("trailingPE"),
        "dividend": info.get("dividendYield"),
        "history": hist
    }