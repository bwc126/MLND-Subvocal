# TODO: Separate EMG data into 50ms windows, run FFT + preprocessing.

class EMG_preparer():

    """ An EMG_preparer prepares EMG data for training a subvocal recognition classification system. Scipy's rfft algorithm is used to yield a fast Fourier transform of our real-numbered data, and return only its real components.

    Attributes:
        window_size: float. Specifies size, in milliseconds, of the Fourier transformed windows to return.
        real_time: boolean. If True, EMG data has real units of time (such as ns or ms). If False, EMG data has sequential sample number as temporal indicator (dimensionless count).
        sample_rate: float. Specifies number of samples per second. Only needed if real_time = False.
        power_spectrum: boolean. Specifies whether to find a power spectrum using the data after FT has been applied. Practically, this means finding the absolute values of the intensities returned by the Fourier transform so all results are positive.

    """
