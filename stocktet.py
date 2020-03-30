# info, dividents, splits, annualfiancnial, quaterlyfinancial, earnings


import yfinance as yf


class Stockreader:

    def __init__(self, info=None, dividends=None, splits=None, financials=None, earnings=None):
        self.info = info
        self.dividends = dividends
        self.splits = splits
        self.financials = financials
        self.earnings = earnings

    def companyinfo(self):
        input_ticker = str(input("Enter a string information:"))
        print(input_ticker)
        return input_ticker

    def passvalue(self):
        return yf.Ticker(self.companyinfo())

    # def tickerinformation(self):
    # return self.info, self.dividends, self.splits, self.financials, self.earnings


stockTickerOne = Stockreader()
some_value = stockTickerOne.passvalue()
print(some_value.info)
