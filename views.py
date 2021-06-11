from django.shortcuts import render
from .models import CE, PE
import pandas as pd
import requests
import datetime
import json


def insert_data(data, ref):
    for value in data:
        reference = CE() if ref == 1 else CE()
        timestamp = datetime.datetime.now()
        reference.timestamp = str(
            timestamp).split('.')[0].replace(' ', '_')  # e.g. YYYY-MM-DD_HH:MM:SS
        reference.strikePrice = value['strikePrice']
        reference.openInterest = value['openInterest']
        reference.changeinOpenInterest = value['changeinOpenInterest']
        reference.totalTradedVolume = value['totalTradedVolume']
        reference.impliedVolatility = value['impliedVolatility']
        reference.lastPrice = value['lastPrice']
        reference.change = value['change']
        reference.pChange = value['pChange']
        reference.bidQty = value['bidQty']
        reference.bidprice = value['bidprice']
        reference.askQty = value['askQty']
        reference.askPrice = value['askPrice']
        reference.save()


def index(request):
    URL = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
    header = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(URL, headers=header)
    datas = json.loads(response.text)
    expiry_dates = [date for date in datas['records']['expiryDates']]
    return render(request, 'index.html', {'expiry_dates': expiry_dates})


def show_result(request):

    URL = f'https://www.nseindia.com/api/option-chain-indices?symbol={request.POST["symbol"]}'
    header = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(URL, headers=header)
    datas = json.loads(response.text)

    expiry_dates = [date for date in datas['records']['expiryDates']]
    raw_ce = [
        data['CE'] for data in datas['records']['data']
        if "CE" in data and data['expiryDate'] == request.POST['expiry_date']]
    raw_pe = [
        data['PE'] for data in datas['records']['data']
        if "PE" in data and data['expiryDate'] == request.POST['expiry_date']]

    insert_data(raw_ce, 1)
    insert_data(raw_pe, 2)

    ce_data = pd.DataFrame(raw_ce).sort_values(['strikePrice'])
    pe_data = pd.DataFrame(raw_pe).sort_values(['strikePrice'])

    return render(request, 'index.html', {
        'expiry_dates': expiry_dates, 'ce_data': ce_data, 'pe_data': pe_data, 'has_data': True})
