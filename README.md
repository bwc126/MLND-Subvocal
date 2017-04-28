# MLND-Subvocal
Udacity MLND Capstone for Subvocal Recognition

Use quick2wire analog board to capture analog signals from dermal electrodes placed near the glossopharyngeal nerve.
Nerve signals are captured while the user subvocalizes sentences.
We then attempt to train a machine learning model to recognize voltage patterns corresponding to specific subvocalized phonemes.

Specifically, the pcf8591read script is run on a raspberry pi with the analog board.
This script writes csv data to file.
The csv data is later used to train a model.

The csv contains time and voltage data.

A unique csv file will be produced for each subvocalization trial. A subvocalization trial consists of single sentence read subvocally three times with 2 seconds of rest between each repetition and 2 seconds before and after the first and last subvocalizations.

The blocks of subvocalization-positive data are then collected in the order they appear, and the user matches them with the sentences or words they subvocalized.
The data is now paired between voltage data and target phonemes to train a supervised model to reconstruct phonemes given voltage data.

## 3-2-2017

Sat Mar 4 data: Consists of select samples from Jane Austen data, the same sentences found in Agile Analyst in the Austen csv file. The following numbers correspond to the sentences read to produce the Mar 4 data, in order: 1,5,6,8,10,13,17,19,20,23,26,27,28,30,31,32,33,34,40,41,42,43


## Update: Preparing for the Capstone

I'll need to clean up this repository to prepare for the MLND Capstone. I'll need to remove all unnecessary code and documentation. Then I'll need to start describing and architecting my approach. Next will come describing and stubbing classes and methods. Then, implementation and results compilation. This step will be iterative and likely involve some bootstrapping with audio data.

The approach chosen for the capstone involves finding articulatory features in the EMG data, a more specific way of looking for phonemes. I'll need to use a MLPC to pick out phonological features from EMG data corresponding to specific phonemes. This will serve as a foundation for future full development of subvocal recognition.

I'll need to discuss my chosen algorithms, and provide a description of metrics and equations (F score). I'll need to create separate clean files for functions and classes, and import into a Jupyter notebook to do development of the main project. I'll need to document every class and function I write. I'll describe my grid search for parameters and discuss the ones I choose.

Note: EMG data recorded at 1000 samples per second. An FFT result of 0.5 cycles per sample means 500 Hz.

### Tentative Sequence:
1. Separate EMG data into 50ms windows, run FFT + preprocessing. (prepare_EMG.py)
2. Label EMG data with phonemes from Austen. (prepare_outputs.py)
3. Decompose phonemes into phonological features. (prepare_outputs.py)
4. Train MLPC to identify phonological features from EMG data, or 'Articulatory Features'. (jupyter notebook)
5. Validate by reconstructing phonemes in unseen data. (jupyter notebook)
