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

MA1 = 5
MA2 = 15

def moving_average(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid')
    return smas

def high_minus_low(highs, lows):
    return highs - lows


def graph_data():
    fig = plt.figure()
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
    plt.ylabel('H-L')
    ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1, sharex = ax1)
    plt.ylabel('Price')
    ax2v = ax2.twinx()

    ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex = ax1)
    plt.ylabel('MAvgs')
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

    h_l = list(map(high_minus_low, highp, lowp))
    ax1.plot_date(date[-start:], h_l[-start:], '-', label='H-L')
    plt.setp(ax1.get_xticklabels(), visible=False)

    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=3, prune='lower'))

    #candlestick_ohlc(ax1, new_list)

    #candlestick_ohlc(ax1, new_list, width=.6, colorup='g', colordown='r')
    candlestick_ohlc(ax2, new_list[-start:], width=.6, colorup='#41ad49', colordown='#ff1717')


    ax2.grid(True) #ax1.grid(True, color = 'g', linestyle='-', linewidth=3)
    plt.setp(ax2.get_xticklabels(), visible=False)
    ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=3, prune='upper'))
    bbox_props = dict(boxstyle='round4, pad=0.3', fc="#c5cbdf", ec='k', lw=2)
    ax2.annotate(str(closep[-1]), (date[-1], closep[-1]),
                 xytext = (date[-1] + 8, closep[-1]), bbox = bbox_props)

    ax2v.fill_between(date[-start:], 0, volume[-start:], facecolor='#0079a3', alpha=0.4)
    ax2v.plot([], [], '-', color='#0079a3', label='Volume', alpha=0.4)
    ax2v.axes.yaxis.set_ticklabels([])
    ax2v.grid(False)
    ax2v.set_ylim(0, 3*volume.max())

    ax3.plot(date[-start:], ma1[-start:], linewidth = 1, label=str(MA1)+'MA')
    ax3.plot(date[-start:], ma2[-start:], linewidth = 1, label=str(MA2)+'MA')
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:], where = (ma2[-start:]>=ma1[-start:]), facecolor = 'r', edgecolor = 'r', alpha = 0.5)
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:], where = (ma2[-start:]<=ma1[-start:]), facecolor = 'g', edgecolor = 'g', alpha = 0.5)
    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=3, prune='upper'))

    plt.subplots_adjust(left=.13, bottom=.26, right=.94, top=.95, wspace=.2, hspace=.2)
    ax1.legend()
    leg = ax1.legend(loc=9, ncol=2, prop={'size':11}, fancybox=True, borderaxespad=0)
    leg.get_frame().set_alpha(0.4)
    ax2v.legend()
    leg = ax2v.legend(loc=9, ncol=2, prop={'size':11}, fancybox=True, borderaxespad=0)
    leg.get_frame().set_alpha(0.4)
    ax3.legend()
    leg = ax3.legend(loc=9, ncol=2, prop={'size':11}, fancybox=True, borderaxespad=0)
    leg.get_frame().set_alpha(0.4)
    plt.show()


graph_data()
