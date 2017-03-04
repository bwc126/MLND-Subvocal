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

3-2-2017

Next steps: Begin recording actual subvocal test data.

Compile a list of text samples. About twenty should do.

For each text sample, begin recording, wait two seconds, subvocalize slowly (at slow reading speed). Wait two seconds, then subvocalize again. Do this a totall of three times for each text sample. Wait two seconds after the last subvocalization, then stop recording for that trial.

We'll then have twenty csv files, each corresponding to a text sample. Each file should have subvocal signals for three repretitions of the text sample. We might have a way of programmatically compositing these repetitions for each sample, then training a model to look for the actual text as 'labels' on the voltage data's features.


Sat Mar 4 data: Consists of select samples from Jane Austen data, the same sentences found in Agile Analyst in the Austen csv file. The following numbers correspond to the sentences read to produce the Mar 4 data, in order: 1,5,6,8,10,13,17,19,20,23,26,27,28,30,31,32,33,34,40,41,42,43
