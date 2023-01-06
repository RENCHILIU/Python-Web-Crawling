import requests

keyword = "AAPL"
URL = "https://finance.yahoo.com/quote/"
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

try:
    r = requests.get(URL+keyword, headers = headers)
    print(r.text)
except:
    print(r.text)
