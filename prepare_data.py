# TODO: Load the csv files into dataframes here.
import csv
import pandas

class data_preparer():
    def __init__(self):
        pass
    def load(self, filename):
        # A simpler method of loading files by filename. Retained for future experimentation. 
        X = pandas.read_csv(filename)
        return X

    def load_singletons(self, series):
        """
        load_singletons reads a file from the simple svr series, where each file should contain only a single word. We take the word from the filename, break it into phonemes, and then return a dataframe containing the raw emg data from the file and an integer representing the number of phonemes in the word. The number of phonemes in the word is useful for splitting the data into specific-sized windows depending on the length of the file and the number of phonemes.

        Outputs
            samples: dict of dataframes, where each key is the word and each value is a dataframe containing an EMG sample for the word.
        """
        svr_words = ['dusty','march','direful','complete','superb','poised','wait','quaint','save','copy','interest','separate','bright','utter','bored','nondescript','license','vest','dance','money','languid','swim','enthusiastic','quartz','planes','spiritual','imperfect','coal','hobbies','sound','bow','squirrel','push','treatment','mine','precede','weather','amazing','round','stingy','signal','marry','country','uncle','dust','certain','loose','knock','advice','confuse','animated','loving','feeling','absorbing','trick','spare','rod','caption','raspy','throne','clumsy','vague','tow','hang','rely','tired','barbarous','pan','innocent','combative','low','rub','mixed','actually','faulty','thirsty','dam','doubtful','flowers','defective','frogs','outstanding','ducks','icicle','fry','load','cracker','efficient','hop','fax','fancy','reading','real','addicted','motion','clean','unsuitable','race','aspiring','gold','check','bouncy','regret','chop','various','eminent','wander','living','equable','cluttered','geese','tightfisted','aftermath','quince','division','board','amuck','pretty','sun','person','magical','invent','flap','stomach','black','river','town','type','stereotyped','paddle','expand','puncture','cakes','measly','kitty','courageous','shoe','number','third','ugliest','haircut','increase','wrathful','jog','straw','whisper','kick','talented','curious']
        samples = {}
        for word in svr_words:
            try:
                filename = 'simple-svr-data/' + word + '-' + str(series)
                samples[word] = pandas.read_csv(filename)
            except Exception as inst:
                print(inst)
        return samples
