from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from yahoo_fin import stock_info
# from yahoo_fin.stock_info import get_data
import yfinance as yf
import time
import queue
from threading import Thread
from asgiref.sync import sync_to_async

# Create your views here.
def stockpicker(request):
    tickers = stock_info.tickers_nifty50()
    print(tickers)
    return render(request, 'mainapp/stockpicker.html', {'stockpickers': tickers})


def stocktracker(request):
    stockpicker = request.GET.getlist('stockpicker')
    print("stockpicker", stockpicker)
    data= {}
    n_threads = len(stockpicker)
    thread_list = []
    que = queue.Queue()
    start = time.time()
    # for ticker in stockpicker:

    #     print("Ticker", ticker)
    #     historical_datas[ticker] = yf.Ticker(ticker).info
    # yf.Ticker(arg1).info
    for i in range(n_threads):
        thread = Thread(target = lambda q, arg1: q.put({stockpicker[i]:  yf.Ticker(arg1).info}), args = (que, stockpicker[i]))
        thread_list.append(thread)
        thread_list[i].start()

    for thread in thread_list:
        thread.join()

    while not que.empty():
        result = que.get()
        data.update(result)
    end = time.time()
    time_taken =  end - start
    print(time_taken)
            
    
    print(data)

    end = time.time()
    timetaken = end-start
    print("Timetaken", timetaken)       
    # print(historical_datas)
      
    return render(request, 'mainapp/stocktracker.html', {"data":data})

def test(request):
   

# Fetch historical data for Apple (AAPL) from 2020-01-01 to 2021-01-01
    symbol = "RELIANCE.NS"
    aapl = yf.Ticker(symbol)

    # Fetch summary information for the symbol
    summary_info = aapl.info
    for key, val in summary_info.items():
        print(f"{key}: {val}")
    
    return HttpResponse("Hello ")
