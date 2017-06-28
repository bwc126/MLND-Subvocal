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
    def __init__(self):
        """ Initializes the output_preparer class.
        """
        pass

    def transform(self, text):
        """ Transforms 'text', a string, into arrays of phonological features corresponding to phonemes. Returns a DataFrame of phonological features and their corresponding phonemes.
        """
        # Get cmu's dictionary of words and phonemes ready.
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
        # Build a dataframe to use as a glossary of phonemes and their AF's.
        pho_AF_map = pandas.DataFrame.from_dict(phonemes, orient='index')
        pho_AF_map.set_axis(1, AF)
        # Make sure we have uniform case before looking up our words.
        text = text.lower()
        words = text.split(" ")
        words = [str().join(filter(str.isalpha, word)) for word in words]
        words = [word for word in words if word]
        # print(words)
        all_phonemes = []
        # We attempt to find each word in the cmudict, to get its phonemes
        for word in words:
            if word in self.arpabet:
                all_phonemes += [phoneme for phoneme in self.arpabet[word][0]]

        # We build a dataframe of output feature vectors for each phoneme in each word.
        vector_frame = pandas.DataFrame()
        for phoneme in all_phonemes:
            pho = ''.join(filter(str.isalpha, phoneme))
            vector_frame = vector_frame.append([pho_AF_map.loc[pho]])



        return vector_frame
