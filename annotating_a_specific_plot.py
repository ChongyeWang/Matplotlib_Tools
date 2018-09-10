import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import urllib
import numpy as np
import datetime as dt
from matplotlib import style



style.use('fivethirtyeight')

def graph_data():
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    plt.ylabel('Price')
    plt.xlabel('Date')

    print('Currently viewing:')
    url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')

    for each_line in split_source:
        split_line = each_line.split(',')
        if 'Date' not in each_line:
            stock_data.append(each_line)


    date, openp, highp, lowp, closep, adjusted_close, volume = np.loadtxt(stock_data, delimiter = ',', \
       unpack = True, converters={0: mdates.bytespdate2num('%Y-%m-%d')})

    x = 0
    y = len(date)
    new_list = []
    while x < y:
        append_line = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        new_list.append(append_line)
        x += 1


    candlestick_ohlc(ax1, new_list, width=.6, colorup='#41ad49', colordown='#ff1717')
    ax1.grid(True) #ax1.grid(True, color = 'g', linestyle='-', linewidth=3)

    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.annotate('Oil Spill!!', (date[25], highp[25]),
                 xytext=(0.8, 0.9), textcoords='axes fraction',
                 arrowprops=dict(facecolor="#585858", color="#585858"))

    plt.ylabel('Price')


    plt.subplots_adjust(left=.09, bottom=.26, right=.94, top=.95, wspace=.2, hspace=.2)
    plt.show()


graph_data()
