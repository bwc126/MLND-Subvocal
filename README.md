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

### Files in this Repo:
+ Folder 'old-svr-data' contains the old, complex datasets that weren't used in the final version.
+ Folder 'simple-svr-data' contains the simpler one word-per-file data that was used to train the solution model.
+ pcf8591read.py is for having an r-pi and q2w ADC read EMG data, it was used to gather EMG data.
+ prepare_data.py is used to load data files as dataframes for the project.
+ prepare_EMG.py is used to help process EMG data into useful info.
+ prepare_outputs.py is used to transform words into phonemes and articulatory feature vectors.
+ simple SVR words.py is a simple file containing the list of words used to generate the simple-svr-data.
+ simple-svr.py is a script used on the r-pi to help manage the recording process.
+ Subvocal.ipynb is the main development notebook used throughout the project development.
+ vis.py was used to help generate graphs used in the capstone report.
+ wavelet_exp.py is just holding onto some code used to generate neat CWT graphs of the EMG data. 
