# Prepare text to become data labels. Decompose phonemes into phonological features.

# TODO: Decide if this will try to automatically detect subvocalizations and attempt to apply phoneme labels in order. That means it needs a trained subvocalization detector. Alternately, it would need an independent source of information about whether a certain window contains a phoneme or not, and applies the labels automatically. Maybe that's done elsewhere completely.

class output_preparer():
    """ Prepares the target data labels. Takes text, transforms it into phonemes, and then decomposes each phoneme into an array of phonological features. These arrays are returned for association with EMG data.
    
    Attributes:

    """
