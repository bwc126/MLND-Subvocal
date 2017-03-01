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
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
def volt_plot(count, data):
    fig, ax = plt.subplots()

    x = np.arange(count-1000, count)
    line, = ax.plot(count, data[count])


    def animate(i):
        line.set_ydata(data[count])  # update the data
        return line,


    # Init only required for blitting to give a clean slate.
    def init():
        line.set_ydata(np.ma.array(x, mask=True))
        return line,

    ani = animation.FuncAnimation(fig, animate, np.arange(count-1000,count), init_func=init,
                                  interval=15, blit=True)
    plt.show()
