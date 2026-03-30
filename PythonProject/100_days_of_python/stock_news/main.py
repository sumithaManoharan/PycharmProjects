import requests as rt
from datetime import datetime as dt, timedelta
from twilio.rest import Client
import time

# api_key = "d59903e1ef0aaf024fcd277c7487ff69"
account_sid = "ACa80a8e534de084fc39325724f09d2aac"
auth_token = "174334a00a3e78f8991c5be372182009"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "20JCEJOBVV71UJJW"
yesterday = (dt.today() - timedelta(days=1)).strftime("%Y-%m-%d")
db_yesterday = (dt.today() - timedelta(days=2)).strftime("%Y-%m-%d")
NEWS_API = f"https://newsapi.org/v2/everything?q=tesla&from={db_yesterday}&to={yesterday}&sortBy=popularity&apiKey=a816952f6ac7459db8b70388eea8e0ff"
STOCK_API = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={API_KEY}"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stocks = rt.get(STOCK_API)
stocks.raise_for_status()
data = stocks.json()
print(data)

last_two_days = list(data["Time Series (Daily)"].values())[0:2]
difference = float(last_two_days[0]["4. close"]) - float(last_two_days[1]["4. close"])
percent = (difference / float(last_two_days[1]["4. close"]) ) * 100
articles = []
if percent >= 3 or percent <= -3:
    news = rt.get(NEWS_API)
    news_data = news.json()["articles"][:3]
    for article in news_data:
        artics = {"title": article["title"], "url": article["url"]}
        articles.append(artics)

client = Client(account_sid,auth_token)
for i in articles:
    if percent >= 3:
        mess = f"TSLA: 🔺{int(percent)}%\ntitle:{i['title']}\nurl:{i['url']}"
    else:
        mess = f"TSLA: 🔻{int(percent)}%\ntitle:{i['title']}\nurl:{i['url']}"
    message = client.messages.create(
            from_="+17543252895",
            body=f"{mess}",
            to="+919994170602",
        )
    time.sleep(20)

print(message.body)






## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

