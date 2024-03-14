import requests
import asyncio
import calendar
import time

from pyppeteer import launch
from datetime import datetime, timezone
from datetime import timedelta
from dateutil import parser

def get_key(key, history):
    return history[key][0]
    
def time_obj(time_str):
    return datetime.strptime(time_str, "%Y-%m-%d")

def get_stock_at(ticker, date, slept=1):
    time.sleep(0.3)
    global user_agent
    end = date + timedelta(days=7);
    start_unix = calendar.timegm(date.utctimetuple());
    end_unix = calendar.timegm(end.utctimetuple());
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&period1={start_unix}&period2={end_unix}"
    try: 
        r = requests.get(url, headers={'User-agent': 'usr'});
        print(url)
        print(r.status_code)
        if r.status_code == 404 or r.status_code == 400:
            return False
        if r.status_code == 429:
            time.sleep(3 * slept)
            return get_stock_at(ticker, date, 3 * slept)
        return r.json()["chart"]["result"][0]["indicators"]["quote"][0]
    except:
        time.sleep(3 * slept)
        return get_stock_at(ticker, date, 3 * slept)

def get_past_difference(current_date, comp_date):
    current = calendar.timegm(time_obj(current_date).utctimetuple())
    past = calendar.timemgm(timeobj(comp_date).utctimetuple())
    diff = current - past
    if diff < 0:
        return 1000000000000
    return diff

def get_market_cap():
    url = "https://telescope-stocks-options-price-charts.p.rapidapi.com/stocks/AAPL"

    querystring = {"modules":"assetProfile,summaryProfile,price"}

    headers = {
        "X-RapidAPI-Key": "eedc051522mshdcac8e3dba59a9ep1db6d8jsne53f95a3c03c",
        "X-RapidAPI-Host": "telescope-stocks-options-price-charts.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

def get_outstanding_shares(ticker, date):
    return asyncio.get_event_loop().run_until_complete(async_get_outstanding_shares(ticker, date))

def not_valid(history):
    if history == False: 
        return True

