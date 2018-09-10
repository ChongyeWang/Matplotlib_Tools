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


#All available style
#print(plt.style.available)

#Find directory
print(plt.__file__)


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
    """
    #date, openp, highp, lowp, closep, adjusted_close, volume = np.loadtxt(stock_data, delimiter = ',', \
    # unpack = True)
    """

    """
    # date_conv = np.vectorize(dt.datetime.fromtimestamp)
    # date = date_conv(date)
    """



    x = 0
    y = len(date)
    new_list = []
    while x < y:
        append_line = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        new_list.append(append_line)
        x += 1



    """
    #ax1.plot(date, closep, '-')
    #ax1.fill_between(date, closep, 400, where=(closep >= 400), facecolor='g', alpha=0.5)
    #ax1.fill_between(date, closep, 200, where=(closep <= 200), facecolor='r', alpha=0.5)
    #ax1.axhline(200, color='r')
    #ax1.axhline(400, color='g')

    #ax1.fill_between(date, closep, 0, alpha=0.5, edgecolor='r')
    #ax1.fill_between(date, closep, 0, alpha=0.5)
    """



    #candlestick_ohlc(ax1, new_list)

    #candlestick_ohlc(ax1, new_list, width=.6, colorup='g', colordown='r')
    candlestick_ohlc(ax1, new_list, width=.6, colorup='#41ad49', colordown='#ff1717')



    ax1.grid(True) #ax1.grid(True, color = 'g', linestyle='-', linewidth=3)


    """
    ax1.yaxis.label.set_color('m')
    ax1.xaxis.label.set_color('c')
    ax1.set_yticks([0, 700, 1400])
    ax1.spines['left'].set_color('c')
    ax1.spines['bottom'].set_color('c')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_linewidth(8)
    ax1.spines['bottom'].set_linewidth(8)
    """



    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    plt.ylabel('Price')


    plt.subplots_adjust(left=.09, bottom=.26, right=.94, top=.95, wspace=.2, hspace=.2)
    plt.show()


graph_data()
