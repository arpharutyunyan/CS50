import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument   ")
elif sys.argv[1].isalpha():
    sys.exit("Command-line argument is not a number")


try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    currency = r.json()
    rate = currency["bpi"]["USD"]["rate"].replace(",", "")
    amount = float(sys.argv[1]) * float(rate)
    print(f"${amount:,.4f}")
    # print(type(r.json()))
except requests.RequestException:
    pass

