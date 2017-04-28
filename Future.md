

## Deferred: Viterbi Algorithm for Speech Recognition

- To use this algorithm for SVR, first we will need start_p, trans_p, emit_p. We can generate these first two on our own, directly from Austen data or elsewhere, or we can try to find an Open Source version for English. The last one, emit_p, will be determined empirically from our data set, since we already know what states generated our data.

- The 'states' possibilities should most likely be phonemes in English. Our observations, 'obs' could be transformed voltage data using the sklearn FunctionTransformer, which might take every 10-100ms of our data, perform cepstrum analysis (FT->abs()->log->IFT) and use that as the observed data for Viterbi.

- The largest challenges here are finding emit_p, and determining appropriate preprocessing for our data. We will need an automated way of mapping states to observations to determine emit_p. Perhaps decision trees or neural nets would be useful here, where the state could be used as a label and the supervised learner would be trained to find observed features for this state. This model could then be used inversely to yield which features a state is likely to produce, and the probability for each.

- Accuracy should be determined on a phoneme or word basis. Word basis would have a larger transition matrix, but would be much sparser. Phoneme basis would be more general but less accurate for our specific data set. In either case, word or phoneme, this must correspond with our chosen possible 'states' for Viterbi.
