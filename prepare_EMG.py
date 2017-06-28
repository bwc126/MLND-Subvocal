# TODO: Separate EMG data into 50ms windows, run FFT + preprocessing.
from pandas import DataFrame
from scipy.fftpack import rfft, rfftfreq
import time
import numpy as np

class EMG_preparer():

    """ An EMG_preparer prepares EMG data for training a subvocal recognition classification system. Scipy's cwt algorithm is used to yield energy spectrum summations for each phoneme in a file.

    Attributes:
        window_size: float. Specifies size, in milliseconds, of the Fourier transformed windows to return.
        real_time: boolean. If True, EMG data has real units of time (such as ns or ms). If False, EMG data has sequential sample number as temporal indicator (dimensionless count).
        sample_rate: float. Specifies number of samples per second.
        power_spectrum: boolean. Specifies whether to find a power spectrum using the data after FT has been applied. Practically, this means finding the absolute values of the intensities returned by the Fourier transform so all results are positive. If false, the raw rfft results are used for each window.

    """
    def __init__(self):
        """ Initialize the EMG_preparer Object. """

        pass

    def process(self, data, num_phonemes=None, wavelets=False):
        """ process is a method for summing CWT energies from EMG data into windows for each phoneme in the file.

        Attributes:
            data: a pandas DataFrame containing subvocalization EMG data processed by CWT, with any number of columns.
        Returns:
            a DataFrame containing summed energy spectrum windows for each phoneme based on an even splitting of the data.
        """

        if num_phonemes:
            num_windows = num_phonemes
            self.samples_per_window = int(data.shape[0]//num_windows)

        if wavelets:
            windows = DataFrame()
            # Go through each row from first index to last for each window
            for window in range(num_windows):
                first_index = int(window * self.samples_per_window)
                last_index = int(first_index + self.samples_per_window)
                data_window = DataFrame(data.iloc[first_index:last_index])
                # Sum up the squares of amplitudes in each column
                new_row = data_window.abs().pow(2).sum(axis=0)
                windows = windows.append(new_row, ignore_index = True)
            # Return all the windows
            return windows
