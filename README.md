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

Next steps: Begin recording actual subvocal test data.

Compile a list of text samples. About twenty should do.

For each text sample, begin recording, wait two seconds, subvocalize slowly (at slow reading speed). Wait two seconds, then subvocalize again. Do this a totall of three times for each text sample. Wait two seconds after the last subvocalization, then stop recording for that trial.

We'll then have twenty csv files, each corresponding to a text sample. Each file should have subvocal signals for three repretitions of the text sample. We might have a way of programmatically compositing these repetitions for each sample, then training a model to look for the actual text as 'labels' on the voltage data's features.


Sat Mar 4 data: Consists of select samples from Jane Austen data, the same sentences found in Agile Analyst in the Austen csv file. The following numbers correspond to the sentences read to produce the Mar 4 data, in order: 1,5,6,8,10,13,17,19,20,23,26,27,28,30,31,32,33,34,40,41,42,43

## Viterbi Algorithm for Speech Recognition

- To use this algorithm for SVR, first we will need start_p, trans_p, emit_p. We can generate these first two on our own, directly from Austen data or elsewhere, or we can try to find an Open Source version for English. The last one, emit_p, will be determined empirically from our data set, since we already know what states generated our data.

- The 'states' possibilities should most likely be phonemes in English. Our observations, 'obs' could be transformed voltage data using the sklearn FunctionTransformer, which might take every 10-100ms of our data, perform cepstrum analysis (FT->abs()->log->IFT) and use that as the observed data for Viterbi.

- The largest challenges here are finding emit_p, and determining appropriate preprocessing for our data. We will need an automated way of mapping states to observations to determine emit_p. Perhaps decision trees or neural nets would be useful here, where the state could be used as a label and the supervised learner would be trained to find observed features for this state. This model could then be used inversely to yield which features a state is likely to produce, and the probability for each.

- Accuracy should be determined on a phoneme or word basis. Word basis would have a larger transition matrix, but would be much sparser. Phoneme basis would be more general but less accurate for our specific data set. In either case, word or phoneme, this must correspond with our chosen possible 'states' for Viterbi.

## Update: Preparing for the Capstone

I'll need to clean up this repository to prepare for the MLND Capstone. I'll need to remove all unnecessary code and documentation. Then I'll need to start describing and architecting my approach. Next will come describing and stubbing classes and methods. Then, implementation and results compilation. This step will be iterative and likely involve some bootstrapping with audio data.

The approach chosen for the capstone involves finding articulatory features in the EMG data, a more specific way of looking for phonemes. I'll need to use a MLPC to pick out phonological features from EMG data corresponding to specific phonemes. This will serve as a foundation for future full development of subvocal recognition.
