# Prepare text to become data labels. Decompose phonemes into phonological features.

# TODO: Decide if this will try to automatically detect subvocalizations and attempt to apply phoneme labels in order. That means it needs a trained subvocalization detector. Alternately, it would need an independent source of information about whether a certain window contains a phoneme or not, and applies the labels automatically. Maybe that's done elsewhere completely.

class output_preparer():
    """ Prepares the target data labels. Takes text, transforms it into phonemes, and then decomposes each phoneme into an array of phonological features. These arrays are returned for association with EMG data.

    Attributes:



    """
    def __init__(subvocal_detector=None):
        """ Initializes the output_preparer class.

        Attributes:
            subvocal_detector: Optional. An estimator trained to detect subvocalizations in EMG windows. This estimator simply returns 'True' or 'False' for whether an EMG window it's passed contains subvocalization. This is only used with the 'zip' method for the output_preparer class when that method's 'auto_align' attribute is True.

        """
        pass

    def transform(text):
        """ Transforms 'text', a string, into arrays of phonological features corresponding to phonemes. Returns a DataFrame of phological features and their corresponding phonemes.
        """
        pass

    def zip(data, labels, auto_align=True):
        """ Zips data and labels such that labels are sequentially applied to serial rows of 'data' that most likely contain subvocalizations. If the data is already boolean labeled for containing subvocalization, 'auto_align' should be false to make use of those labels.

        Attributes:
            data: a pandas DataFrame containing rows of subsequent EMG windows.
            labels: a pandas DataFrame of phonological features and phonemes.
            auto_align: boolean. If true, indicates an automatic method is to be used in aligning each row in 'outputs' with those portions of 'data' most likely to contain actual subvocalization.
        Returns:
            A dataframe of labels with null values where corresponding rows in 'data' most likely do not contain subvocalization, or are labeled as such.
        """
        pass
