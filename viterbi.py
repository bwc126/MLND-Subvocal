# The Viterbi algorithm, from https://en.wikipedia.org/wiki/Viterbi_algorithm#Example

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    for st in states:
        V[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}
    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for st in states:
            max_tr_prob = max(V[t-1][prev_st]["prob"]*trans_p[prev_st][st] for prev_st in states)
            for prev_st in states:
                if V[t-1][prev_st]["prob"] * trans_p[prev_st][st] == max_tr_prob:
                    max_prob = max_tr_prob * emit_p[st][obs[t]]
                    V[t][st] = {"prob": max_prob, "prev": prev_st}
                    break
    for line in dptable(V):
        print line
    opt = []
    # The highest probability
    max_prob = max(value["prob"] for value in V[-1].values())
    previous = None
    # Get most probable state and its backtrack
    for st, data in V[-1].items():
        if data["prob"] == max_prob:
            opt.append(st)
            previous = st
            break
    # Follow the backtrack till the first observation
    for t in range(len(V) - 2, -1, -1):
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]
    print 'The steps of states are ' + ' '.join(opt) + ' with highest probability of %s' % max_prob

def dptable(V):
    # Print a table of steps from dictionary
    yield " ".join(("%12d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)

# To use this algorithm for SVR, first we will need start_p, trans_p, emit_p. We can generate these first two on our own, directly from Austen data or elsewhere, or we can try to find an Open Source version for English. The last one, emit_p, will be determined empirically from our data set, since we already know what states generated our data.

# The 'states' possibilities should most likely be phonemes in English. Our observations, 'obs' could be transformed voltage data using the sklearn FunctionTransformer, which might take every 10-100ms of our data, perform cepstrum analysis (FT->abs()->log->IFT) and use that as the observed data for Viterbi.

# The largest challenges here are finding emit_p, and determining appropriate preprocessing for our data. We will need an automated way of mapping states to observations to determine emit_p. Perhaps decision trees or neural nets would be useful here, where the state could be used as a label and the supervised learner would be trained to find observed features for this state. This model could then be used inversely to yield which features a state is likely to produce, and the probability for each.

# Accuracy should be determined on a phoneme or word basis. Word basis would have a larger transition matrix, but would be much sparser. Phoneme basis would be more general but less accurate for our specific data set. In either case, word or phoneme, this must correspond with our chosen possible 'states' for Viterbi.
