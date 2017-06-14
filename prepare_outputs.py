# Prepare text to become data labels. Decompose phonemes into phonological features.

import nltk, pandas, prepare_data, prepare_EMG
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ShuffleSplit
from sklearn.svm import SVC
import numpy as np

class output_preparer():
    """ Prepares the target data labels. Takes text, transforms it into phonemes, and then decomposes each phoneme into an array of phonological features. These arrays are returned for association with EMG data.

    Attributes:
        subvocal_detector: Optional. An estimator trained to detect subvocalizations in EMG windows. This estimator simply returns 'True' or 'False' for whether an EMG window it's passed contains subvocalization. This is only used with the 'zip' method for the output_preparer class when that method's 'auto_align' attribute is True.
    """
    def __init__(self, subvocal_detector=None, window_size=30.0, do_grid_search=False, use_auto=False):
        """ Initializes the output_preparer class.
        """
        self.window_size = window_size
        self.detector = subvocal_detector
        self.do_grid_search = do_grid_search
        if use_auto and not self.detector:
            if self.do_grid_search:
                self.build_autodetector()
            else:
                estimator = SVC(C=0.45, kernel='rbf', random_state=12, gamma=0.45)
                data_prep = prepare_data.data_preparer()
                # Use samples from each of the files that are both certain to contain and certain to not contain subvocalizations
                EMG_Prep = prepare_EMG.EMG_preparer(window_size=self.window_size)
                x_1, x_2 = data_prep.sv_detection()
                # Get some select samples
                X_1, X_2 = EMG_Prep.process(x_1), EMG_Prep.process(x_2)
                labels = []
                for row in range(X_1.shape[0]):
                    labels.append(0)
                for row in range(X_2.shape[0]):
                    labels.append(1)
                X = X_1.append(X_2)
                labels = pandas.DataFrame(np.ravel(labels), index=[i for i in range(len(labels))], columns=['sv'])
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
        self.arpabet = nltk.corpus.cmudict.dict()

        # Each phoneme has four features, one for each category: Manner, Place, Height, and Vowel. These features will be used to train feature extractors which will be combined with the MLPC to better identify phonemes from EMG data. For the capstone, we're ignoring variations on these phonemes, we'll remove any numerals from the phonemes returned by nltk so they match with these phonemes. This will help control complexity of the model and system somewhat.
        phonemes = {
        ' ': ['silent', 'silent', 'silent', 'silent'],
        'AA': ['vowel', 'back', 'low', 'yes'],
        'AE': ['vowel', 'mid-front', 'low', 'yes'],
        'AH': ['vowel', 'mid', 'mid', 'yes'],
        'AO': ['vowel','back','mid-low','yes'],
        'AW': ['vowel','mid-front','low','yes'],
        'AY': ['vowel','back','low','yes'],
        'B': ['voiced-stop','labial','max','no'],
        'CH': ['stop','front','max','no'],
        'D': ['voiced-stop','alveolar','max','no'],
        'DH': ['voiced-fricative','dental','max','no'],
        'EH': ['vowel','mid-front','mid','yes'],
        'ER': ['vowel','mid','mid','yes'],
        'EY': ['vowel','front','mid-high','yes'],
        'F': ['fricative','labial','max','no'],
        'G': ['voiced-stop','dorsal','max','no'],
        'HH': ['aspirated','unknown','max','no'],
        'IH': ['vowel','mid-front','high','yes'],
        'IY': ['vowel','front','very high','yes'],
        'JH': ['voiced-stop','front','max','no'],
        'K': ['stop','dorsal','max','no'],
        'L': ['approximant','lateral','very high','no'],
        'M': ['nasal','labial','max','no'],
        'N': ['nasal','alveolar','max','no'],
        'NG': ['nasal','dorsal','max','no'],
        'OW': ['vowel','back','mid','yes'],
        'OY': ['vowel','back','mid-low','yes'],
        'P': ['stop','labial','max','no'],
        'R': ['approximant','retroflex','mid-low','no'],
        'S': ['fricative','alveolar','max','no'],
        'SH': ['fricative','front','max','no'],
        'T': ['stop','alveolar','max','no'],
        'TH': ['fricative','dental','max','no'],
        'UH': ['vowel','mid-back','high','yes'],
        'UW': ['vowel','back','very-high','yes'],
        'V': ['voiced-fricative','labial','max','no'],
        'W': ['approximant','back','very-high','no'],
        'Y': ['approximant','front','very-high','no'],
        'Z': ['voiced-fricative','alveolar','max','no'],
        'ZH': ['voiced-fricative','front','max','no']}
        AF = ['manner', 'place', 'height', 'vowel']
        pho_AF_map = pandas.DataFrame.from_dict(phonemes, orient='index')
        # pho_AF_map = pandas.DataFrame(pho_AF_map, columns=AF)
        pho_AF_map.set_axis(1, AF)
        # print(pho_AF_map.head())
        text = text.lower()
        words = text.split(" ")
        words = [str().join(filter(str.isalpha, word)) for word in words]
        words = [word for word in words if word]
        # print(words)
        all_phonemes = []
        for word in words:
            if word in self.arpabet:
                all_phonemes += [phoneme for phoneme in self.arpabet[word][0]]

        # print(all_phonemes)
        vector_frame = pandas.DataFrame()
        for phoneme in all_phonemes:
            pho = ''.join(filter(str.isalpha, phoneme))
            vector_frame = vector_frame.append([pho_AF_map.loc[pho]])
            # print(pho)

        # print (vector_frame)
        return vector_frame

    def zip(self, data, labels, auto_align=True, repeat=1):
        """ Zips data and labels such that labels are sequentially applied to serial rows of 'data' that most likely contain subvocalizations. This is accomplished by dropping rows of 'data' that appear to lack subvocalization. If the data is already boolean labeled for containing subvocalization, 'auto_align' should be false to make use of those labels.

        Attributes:
            data: a pandas DataFrame containing rows of subsequent EMG windows.
            labels: a pandas DataFrame of phonological features and phonemes.
            auto_align: boolean. If true, indicates an automatic method is to be used in aligning each row in 'outputs' with those portions of 'data' most likely to contain actual subvocalization.
            repeat: int. Number of times the full list of labels is expected to appear within 'data'.
        Returns:
            A dataframe of processed EMG windows that are marked as likely to contain subvocalization.
        """
        # We handle repetitions of labels within data by multiplying the dataframe of labels. The whole dataframe is repeated however many times we expect the labels to appear in the data.
        for i in range(repeat-1):
            # print('we make labels longer by one whole')
            labels = labels.append(labels)
        # We prepare the new, aligned labels dataframe
        AF = ['manner', 'place', 'height', 'vowel']
        new_labels = pandas.DataFrame(columns=AF)
        # Initially, we begin with the very first row of labels. This'll be iterated every time we find a row in the data that seems to contain subvocalization.
        new_data = pandas.DataFrame(columns=data.axes[1])
        label_row = 0
        null_row = pandas.DataFrame.from_dict({" ": ['silent', 'silent', 'silent', 'silent']}, orient='index')
        null_row.set_axis(1,AF)
        if auto_align:
            method = self.detector.predict
        else:
            method = lambda x: x[row]['subvocalization'] == True
        # For row in data
        # for row in data.iterrows():
        #     series = row[1]
        #     # If row appears or is marked as containing subvocalization
        #     if method(series.values.reshape(1,-1)):
        #         print('yes')
        #         if label_row >= labels.shape[0]:
        #             new_labels = new_labels.append(null_row)
        #         else:
        #             # Apply next phoneme label to that row
        #             new_labels = new_labels.append(labels.iloc[label_row])
        #         label_row += 1
        #     else:
        #         print('no')
        #         new_labels = new_labels.append(null_row)
        # return new_labels
        #
        # Instead of taking outputs and applying null rows to most of the data, just drop all the data that doesn't appear to contain subvocalization. That should have a similar effect while reducing the null data.
        for row in data.iterrows():
            series = row[1]
            # print('row:',row[0])
            # If row appears or is marked as containing subvocalization
            if method(series.values.reshape(1,-1)):
                # print('yes')
                if label_row < labels.shape[0]:
                    new_data = new_data.append(data.iloc[row[0]],ignore_index=True)

                # Apply next phoneme label to that row
                # new_data = new_data.append(labels.iloc[label_row])
                label_row += 1
            # else:
                # print('no')
                # new_labels = new_labels.append(null_row)
        # print(labels)
        return new_data, labels
    def build_autodetector(self):
        """
        This method can perform gridsearch to find autodetector parameters.
        """
        estimator = SVC()
        param_grid = {
            'C': [0.45,0.5,0.55],
            'kernel': ['rbf'],
            'gamma': [0.45,0.5,0.55],
        }
        cv = ShuffleSplit(n_splits=3, test_size=0.15, random_state=3)
        grid_search = GridSearchCV(SVC(), param_grid, n_jobs=-1, cv=cv)
        data_prep = prepare_data.data_preparer()
        # Use samples from each of the files that are both certain to contain and certain to not contain subvocalizations
        EMG_Prep = prepare_EMG.EMG_preparer(window_size=self.window_size)
        x_1, x_2 = data_prep.sv_detection()
        # Get some select samples
        X_1, X_2 = EMG_Prep.process(x_1), EMG_Prep.process(x_2)
        labels = []
        for row in range(X_1.shape[0]):
            labels.append(0)
        for row in range(X_2.shape[0]):
            labels.append(1)
        X = X_1.append(X_2)
        labels = pandas.DataFrame(np.ravel(labels), index=[i for i in range(len(labels))], columns=['sv'])
        print(X.shape,labels.shape)
        grid_search.fit(X, labels)
        print("Training Score:", grid_search.score(X, labels))
        self.cv_results = grid_search.cv_results_
        self.detector = grid_search.best_estimator_
        # Process them into windows
        # Combine those windows with 'yes' or 'no' labels for SV
        # Train an estimator on these datapoints to identify SV signals in windows
