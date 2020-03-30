import yfinance as yf


class stock_app:

    def __init__(self, info=None):
        self.info = info

    def company(self):
        self.value = str(input("Enter compant ticker:"))
        return self.value

    def ticker_info(self):
        return yf.Ticker(self.company())  # calling a function


stock_app_object = stock_app()
company_name = stock_app_object.ticker_info()

print(company_name)

price_dict = company_name.info
print(price_dict)
