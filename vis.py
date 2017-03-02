# """
# ===========
# Random data
# ===========
#
# An animation of random data.
#
# """
#
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
# fig, ax = plt.subplots()
# line, = ax.plot(np.random.rand(256))
# ax.set_ylim(0, 1)
#
#
# def update(data):
#     line.set_ydata(data)
#     return line,
#
#
# def data_gen():
#     while True:
#         yield np.random.rand(256)
#
# ani = animation.FuncAnimation(fig, update, data_gen, interval=100)
# plt.show()
"""
A simple example of an animated plot
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def test_plot():
    fig, ax = plt.subplots()

    x = np.arange(-60, 0, .01)
    line, = ax.plot(x, np.sin(x))


    def animate(i):
        line.set_ydata(np.sin(x + i/10.0))  # update the data
        return line,


    # Init only required for blitting to give a clean slate.
    def init():
        line.set_ydata(np.ma.array(x, mask=True))
        return line,

    ani = animation.FuncAnimation(fig, animate, np.arange(1, 2000), init_func=init,
                                  interval=25, blit=True)
    plt.show()

"""
A simple example of an animated plot
"""
def volt_plot(datafile):
    fig, ax = plt.subplots()
    x, y = [], []
    with open(datafile) as csvfile:
        filereader = csv.reader(csvfile,delimiter=',')
        for row in filereader:
            x.append(row[0])
            y.append(row[1])
    print(x[0], y[0])
    x, y = x[1:], y[1:]
    print(x[0], y[0])
    line, = ax.plot(x, y, label='voltage')


    # def animate(i):
    #     line.set_ydata(data[count])  # update the data
    #     return line,
    #

    # Init only required for blitting to give a clean slate.
    # def init():
    #     line.set_ydata(np.ma.array(x, mask=True))
    #     return line,

    # ani = animation.FuncAnimation(fig, animate, np.arange(count-1000,count), init_func=init,
    #                               interval=15, blit=True)
    plt.show()

volt_plot('Thu Mar  2 23:04:12 2017')
