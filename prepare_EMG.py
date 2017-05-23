# TODO: Separate EMG data into 50ms windows, run FFT + preprocessing.
from pandas import DataFrame
from scipy.fftpack import rfft, rfftfreq
import time
import numpy as np

class EMG_preparer():

    """ An EMG_preparer prepares EMG data for training a subvocal recognition classification system. Scipy's rfft algorithm is used to yield a fast Fourier transform of our real-numbered data, and return only its real components.

    Attributes:
        window_size: float. Specifies size, in milliseconds, of the Fourier transformed windows to return.
        real_time: boolean. If True, EMG data has real units of time (such as ns or ms). If False, EMG data has sequential sample number as temporal indicator (dimensionless count).
        sample_rate: float. Specifies number of samples per second.
        power_spectrum: boolean. Specifies whether to find a power spectrum using the data after FT has been applied. Practically, this means finding the absolute values of the intensities returned by the Fourier transform so all results are positive. If false, the raw rfft results are used for each window.

    """
    def __init__(self, window_size=50.0, real_time=False, sample_rate=1000, power_spectrum=True):
        """ Initialize the EMG_preparer Object. """
        self.window_size = window_size
        self.samples_per_window = sample_rate / 1000.0 * self.window_size
        self.power_spectrum = power_spectrum
    def process(self, data):
        """ process is a method for processing EMG data into Fourier-transformed windows

        Attributes:
            data: a pandas DataFrame containing subvocalization EMG data and having two columns, "time", and "voltage"
        Returns:
            a DataFrame containing FFT processed windows derived from the EMG data.
        """
        # print (time.clock(), data['voltage'][1], data['voltage'][0])
        num_windows = int(data.shape[0]//self.samples_per_window)
        windows = DataFrame()
        for window in range(num_windows):
            first_index = int(window * self.samples_per_window)
            last_index = int(first_index + self.samples_per_window)
            omega = rfftfreq(last_index - first_index, d=int(data["time"][1])-int(data["time"][0]))
            freq_signal = rfft(data["voltage"][first_index:last_index])
            if self.power_spectrum:
                freq_signal = np.abs(freq_signal)
            # Put the transformed EMG data in the dataframe such that each column is a frequency and each row is a distinct window. The value in a cell will be the power.
            # print (freq_signal, omega)
            new_row = DataFrame(np.reshape(freq_signal, (1,50)), index=[0], columns=omega)
            # new_row = DataFrame.from_items([(freq, om) for freq in freq_signal for om in omega])
            # print(new_row)
            windows = windows.append(new_row, ignore_index=True)
        print (windows)
        return windows
