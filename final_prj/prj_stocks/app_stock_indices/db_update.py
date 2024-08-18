from pathlib import Path
import os
import sqlite3
from django.conf import settings

from fetch_stocks import Class_StockMarketPrices, company_symbol_tickers

BASE_DIR = Path(__file__).resolve().parent.parent
db_address = os.path.join(BASE_DIR, "db.sqlite3")

# for data in self.db_records:
#     symbol = data[0]
#     price = str(data[1])
#     INSERT_DB_DATA = "INSERT INTO STOCK_PRICE_TICKER (stock_symbol, stock_price) VALUES(" + symbol + ', ' + price + ')  ON CONFLICT(stock_symbol) DO UPDATE SET stock_price=' + 'price;'
#     cursor_obj.execute(INSERT_DB_DATA)


class Class_Db_Insert_and_Update:


    def __init__(self, db_data):
        self.db_records = db_data


    def db_update(self):
        conn = sqlite3.connect(db_address)
        cursor_obj = conn.cursor()

        fetch_stock_symbols_db_records = "SELECT stock_symbol from STOCK_PRICE_TICKER;"
        cursor_obj.execute(fetch_stock_symbols_db_records)
        existing_symbols_list = cursor_obj.fetchall()
        conn.commit()

        deletion_list = [i for i in existing_symbols_list if i not in company_symbol_tickers]
        insertion_list = [i for i in company_symbol_tickers if i not in existing_symbols_list]

        insert_stock_symbol_db_record = "Insert into stock_price_ticker(stock_symbol) values(MSFT);"
        # for i in insertion_list:
        #     print(i)
        #     insert_stock_symbol_db_record += i+ """)"""
        #     print(insert_stock_symbol_db_record)
        cursor_obj.execute(insert_stock_symbol_db_record)

        conn.commit()
        conn.close()

if __name__ == "__main__":

    cls_stockmarket_prices = Class_StockMarketPrices(company_symbol_tickers)
    stock_price_data = cls_stockmarket_prices.fetch_prices()


    cls_instance = Class_Db_Insert_and_Update(stock_price_data)
    cls_instance_db = cls_instance.db_update()
