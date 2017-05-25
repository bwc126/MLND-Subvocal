# Prepare text to become data labels. Decompose phonemes into phonological features.

import nltk, pandas, prepare_data, prepare_EMG
from sklearn.svm import SVC
import numpy as np

class output_preparer():
    """ Prepares the target data labels. Takes text, transforms it into phonemes, and then decomposes each phoneme into an array of phonological features. These arrays are returned for association with EMG data.

    Attributes:
        subvocal_detector: Optional. An estimator trained to detect subvocalizations in EMG windows. This estimator simply returns 'True' or 'False' for whether an EMG window it's passed contains subvocalization. This is only used with the 'zip' method for the output_preparer class when that method's 'auto_align' attribute is True.
    """
    def __init__(self, subvocal_detector=None):
        """ Initializes the output_preparer class.
        """
        self.detector = subvocal_detector
        if not self.detector:
            estimator = SVC(C=0.25, kernel='poly', degree=5, random_state=12)
            data_prep = prepare_data.data_preparer()
            # Use samples from each of the files that are both certain to contain and certain to not contain subvocalizations
            EMG_Prep = prepare_EMG.EMG_preparer()
            x_1, x_2 = data_prep.sv_detection()
            # print("sample dataframes: ",x_1,x_2)

            # Get some select samples
            X_1, X_2 = EMG_Prep.process(x_1), EMG_Prep.process(x_2)
            # print("processed sample dataframes: ",X_1,X_2)
            labels = []
            for row in range(X_1.shape[0]):
                # print('lol')
                labels.append(0)
            # for row in X_2:
            for row in range(X_2.shape[0]):
                # print('wut')
                labels.append(1)
            # print(labels)
            X = X_1.append(X_2)
            labels = pandas.DataFrame(np.ravel(labels), index=[i for i in range(len(labels))], columns=['sv'])
            # print(labels['sv'])
            estimator.fit(X, labels)
            print("Training Score:", estimator.score(X, labels))
            self.detector = estimator
            # Process them into windows
            # Combine those windows with 'yes' or 'no' labels for SV
            # Train an estimator on these datapoints to identify SV signals in windows
            pass

    def transform(self, text):
        """ Transforms 'text', a string, into arrays of phonological features corresponding to phonemes. Returns a DataFrame of phonological features and their corresponding phonemes.
        """
        arpabet = nltk.corpus.cmudict.dict()
        words = text.split(" ")
        all_phonemes = []
        for word in words:
            all_phonemes += [phoneme for phoneme in arpabet[word][0]]
            # TODO: Construct arrays of phonological features for each phoneme.
        print(all_phonemes)
        return all_phonemes

    def zip(self, data, labels, auto_align=True):
        """ Zips data and labels such that labels are sequentially applied to serial rows of 'data' that most likely contain subvocalizations. If the data is already boolean labeled for containing subvocalization, 'auto_align' should be false to make use of those labels.

        Attributes:
            data: a pandas DataFrame containing rows of subsequent EMG windows.
            labels: a pandas DataFrame of phonological features and phonemes.
            auto_align: boolean. If true, indicates an automatic method is to be used in aligning each row in 'outputs' with those portions of 'data' most likely to contain actual subvocalization.
        Returns:
            A dataframe of labels with null values where corresponding rows in 'data' most likely do not contain subvocalization, or are labeled as such.
        """
        # For row in data
        # If row appears or is marked as containing subvocalization
        # Apply next phoneme label to that row
        new_labels = DataFrame()
        label_row = 0
        null_row = 0 # TODO: rewrite this to dynamically scale to 'labels', to act as a null filler row. There might be an integrated method for this already.
        if auto_align:
            method = self.detector.predict()
        else:
            method = lambda x: x[row]['subvocalization'] == True
        for row in data:
            if method(data[row]):
                new_labels[row] = labels[label_row]
                label_row += 1
            else:
                new_labels[row] = null_row
        return new_labels
