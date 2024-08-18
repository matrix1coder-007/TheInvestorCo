from django.db import models


# Create your models here.
class StocksSymbolModel(models.Model):

    stock_pkey = models.AutoField(primary_key=True, editable=False)
    stock_symbol = models.CharField(max_length=10, unique=True)
    stock_price = models.TextField()


    def __str__(self):
        return self.stock_symbol + "--" + str(self.stock_price)


    class Meta:
        abstract = False
        db_table = "Stock_Price_Ticker"
        verbose_name = "Stock Price Ticker"
        verbose_name_plural = "Stock Price Tickers"

