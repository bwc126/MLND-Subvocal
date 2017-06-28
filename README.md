# MLND-Capstone: Sub-vocal Recognition
Udacity MLND Capstone for Subvocal Recognition

Using quick2wire analog board, analog signals are captured from dermal electrodes placed near the glossopharyngeal nerve.
Nerve signals are captured while the user fully or sub-vocalizes sentences.
We then attempt to train a machine learning model to recognize voltage patterns corresponding to specific sub-vocalized phonemes.

Specifically, the pcf8591read script is run on a raspberry pi with the analog board.
This script writes csv data to file.
The csv data is later used to train a model.

The csv data from the EMG contains time and voltage data.

A unique csv file was produced for each sub-vocalization trial. A sub-vocalization trial consists of single word read aloud or sub-vocally.

### Development Sequence:
1. Record EMG Data. (r-pi, ADC)
2. Process EMG to extract useful information about MUAP's. (jupyter)
2. Label EMG data with phonemes. (jupyter)
3. Decompose phonemes into phonological features. (prepare_outputs.py)
4. Train MLPC's to identify phonological features and phoenemes from EMG data, or 'Articulatory Features'. (jupyter)
5. Validate by reconstructing phonemes in unseen data. (jupyter)

### Using the Solution Model:
1. Ensure all software pre-req's are met for the processing (non-recording) side of things. Scipy, pandas, and numpy are the main pre-req's.
2. Load 'Subvocal.ipynb' in jupyter notebook.
3. Run through the workflow to see progression of EMG -> MUAP Info -> AF's -> Phonemes.













## 3-2-2017

Sat Mar 4 data: Consists of select samples from Jane Austen data, the same sentences found in Agile Analyst in the Austen csv file. The following numbers correspond to the sentences read to produce the Mar 4 data, in order: 1,5,6,8,10,13,17,19,20,23,26,27,28,30,31,32,33,34,40,41,42,43
