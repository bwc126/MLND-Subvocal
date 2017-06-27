# Used to test animations, generate some EMG graphs in final report.
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


def volt_plot(datafile):
    fig, ax = plt.subplots()
    plt.title('volt plot of ' + datafile)
    x, y = [], []
    with open(datafile) as csvfile:
        filereader = csv.reader(csvfile,delimiter=',')
        for row in filereader:
            x.append(row[0])
            y.append(row[2])
    print(x[0], y[0])
    x, y = x[1:], y[1:]
    print(x[0], y[0])
    line, = ax.plot(x, y, label='voltage')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Voltage (volts)')

    plt.show()

volt_plot('simple-svr-data/advice-2')
volt_plot('simple-svr-data/advice-3')
volt_plot('simple-svr-data/aspiring-1')
volt_plot('simple-svr-data/amuck-2')


from scipy.fftpack import rfft, irfft, rfftfreq

def freq_plot(datafile):
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
    omega = rfftfreq(len(y), d=int(x[1])-int(x[0]))
    freq_signal = rfft(y)
    plt.plot(omega, np.abs(freq_signal), label='voltage')
    plt.xlim(0.001,1)
    plt.ylim(-100,100)

    plt.show()

# freq_plot('Sat Mar  4 00:44:23 2017')
# freq_plot('Sat Mar  4 00:45:02 2017')
# freq_plot('Sat Mar  4 00:45:47 2017')
# freq_plot('Sat Mar  4 00:47:01 2017')
# freq_plot('00:44:23 no sv')
