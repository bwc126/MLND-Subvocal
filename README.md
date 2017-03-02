# MLND-Subvocal
Udacity MLND Capstone for Subvocal Recognition

Use quick2wire analog board to capture analog signals from dermal electrodes placed near the glossopharyngeal nerve. 
Nerve signals are captured while the user subvocalizes sentences.
We then attempt to train a machine learning model to recognize voltage patterns corresponding to specific subvocalized phonemes. 

Specifically, the pcf8591read script is run on a raspberry pi with the analog board.
This script writes csv data to file. 
The csv data is later used to train a model.

The csv contains time and voltage data and whether or not the voltage data contiain subvocalizations.
The subvocalization column of the data contains 'N' if the user was not holding the 'record' key, and 'Y' if they were, indicating a subvocalization.

The blocks of subvocalization-positive data are then collected in the order they appear, and the user matches them with the sentences or words they subvocalized. 
The data is now paired between voltage data and target phonemes to train a supervised model to reconstruct phonemes given voltage data. 
