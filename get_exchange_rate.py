from urllib.request import urlopen
import json

class get_exchange_rate():
    def __init__(self, currency):
        self.generate(currency)
    
    def generate(self, currency):
        self.url = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/chf.json"
        self.page = urlopen(self.url)
        self.data_json = json.loads(self.page.read())
        self.exchange_rate = self.data_json["chf"][currency]
        return self.exchange_rate
    

#testing
if __name__ == '__main__':
    currency = input("For which currency would you like to get the exchange rate?")
    currency = currency.lower()
    exchange_rate = get_exchange_rate(currency)
    print("The current exchange rate from CHF to", currency.upper(),"is",round(exchange_rate.exchange_rate,2))
    del currency
    del exchange_rate
else:
    pass
