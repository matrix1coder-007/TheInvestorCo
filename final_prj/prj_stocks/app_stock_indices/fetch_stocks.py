import yfinance as yf


company_symbol_tickers = [
    'MSFT',
    'GOOG',
    'GOOGL',
    'AMZN',
    'AAPL',
    'BRK-A',
    'BRK-B',
    'COKE',
    'PYPL',
    'TSLA',
    'IBM',
    'WMT',
    'COST',
    'MA',
    'ORCL',
    'F',
    'T',
    'DIS',
    'AI',
    'GM',
    'BABA'    
]


class Class_StockMarketPrices:
    
    def __init__(self, stock_tickers):
        self.stock_tickers = stock_tickers


    def fetch_prices(self) -> list():

        stock_ticker_list = []

        for company_symbol in self.stock_tickers:
            company_ticker = yf.Ticker(company_symbol)
            current_stock_market_price = round(company_ticker.info['currentPrice'], 2)
            stock_ticker_list.append((company_symbol, current_stock_market_price))    

        return stock_ticker_list


if __name__ == "__main__":

    cls_instance = Class_StockMarketPrices(company_symbol_tickers)
    cls_prices = cls_instance.fetch_prices()
    # print('cls-prices', cls_prices)
