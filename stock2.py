import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import urllib
import numpy as np
import datetime as dt
from matplotlib import style


#style.use('ggplot')
#style.use('dark_background')
#style.use('bmh')
style.use('fivethirtyeight')

MA1 = 10
MA2 = 30

def moving_average(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid')
    return smas


def graph_data():
    fig = plt.figure()
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1)
    plt.ylabel('Price')
    ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1)

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


    ma1 = moving_average(closep, MA1)
    ma2 = moving_average(closep, MA2)
    start = len(date[MA2-1:])


    x = 0
    y = len(date)
    new_list = []
    while x < y:
        append_line = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        new_list.append(append_line)
        x += 1


    #candlestick_ohlc(ax1, new_list)

    #candlestick_ohlc(ax1, new_list, width=.6, colorup='g', colordown='r')
    candlestick_ohlc(ax2, new_list, width=.6, colorup='#41ad49', colordown='#ff1717')



    ax2.grid(True) #ax1.grid(True, color = 'g', linestyle='-', linewidth=3)


    for label in ax2.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))


    ax3.plot(date[-start:], ma1[-start:])
    ax3.plot(date[-start:], ma2[-start:])

    plt.subplots_adjust(left=.09, bottom=.26, right=.94, top=.95, wspace=.2, hspace=.2)
    plt.show()


graph_data()
