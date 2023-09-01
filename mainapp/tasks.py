from celery import shared_task
from yahoo_fin.stock_info import *
from threading import Thread
import yfinance as yf
import queue
import json

import asyncio
@shared_task(bind = True)
def update_stock(self, stockpicker):
    data = {}
    available_stocks = tickers_nifty50()
    for i in stockpicker:
        if i in available_stocks:
            pass
        else:
            stockpicker.remove(i)
    
    n_threads = len(stockpicker)
    thread_list = []
    que = queue.Queue()
    for i in range(n_threads):
        thread = Thread(target = lambda q, arg1: q.put({stockpicker[i]: json.loads(json.dumps(yf.Ticker(arg1).info))}), args = (que, stockpicker[i]))
        thread_list.append(thread)
        thread_list[i].start()

    for thread in thread_list:
        thread.join()

    while not que.empty():
        result = que.get()
        data.update(result)
    return " Done Riyad Vai "
