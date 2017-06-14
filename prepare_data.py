# TODO: Load the csv files into dataframes here.
import csv
import pandas

class data_preparer():
    def __init__(self):
        pass
    def load(self, filename):
        # X = pandas.DataFrame()
        # with open(filename) as csvfile:
        #     filereader = csv.reader(csvfile,delimiter=',')
        X = pandas.read_csv(filename)
        return X
    def sv_detection(self):
        data_1 = pandas.read_csv('Sat Mar  4 00:44:23 2017')
        data_2 = pandas.read_csv('Sat Mar  4 00:45:02 2017')
        data_3 = pandas.read_csv('Sat Mar  4 00:45:47 2017')
        data_4 = pandas.read_csv('Sat Mar  4 00:47:01 2017')
        data_5 = pandas.read_csv('Sat Mar  4 00:47:36 2017')
        data_6 = pandas.read_csv('Sat Mar  4 00:48:09 2017')
        data_7 = pandas.read_csv('Sat Mar  4 00:49:05 2017')
        data_8 = pandas.read_csv('Sat Mar  4 00:49:41 2017')
        data_9 = pandas.read_csv('Sat Mar  4 00:50:22 2017')
        data_10 = pandas.read_csv('Sat Mar  4 00:51:17 2017')
        data_11 = pandas.read_csv('Sat Mar  4 00:52:02 2017')
        data_12 = pandas.read_csv('Sat Mar  4 00:52:38 2017')
        data_13 = pandas.read_csv('Sat Mar  4 00:53:24 2017')
        data_14 = pandas.read_csv('Sat Mar  4 00:53:51 2017')
        data_15 = pandas.read_csv('Sat Mar  4 00:54:25 2017')
        data_16 = pandas.read_csv('Sat Mar  4 00:54:57 2017')
        data_17 = pandas.read_csv('Sat Mar  4 00:56:01 2017')
        data_18 = pandas.read_csv('Sat Mar  4 00:56:35 2017')
        data_19 = pandas.read_csv('Sat Mar  4 00:57:21 2017')
        data_20 = pandas.read_csv('Sat Mar  4 00:57:49 2017')
        data_21 = pandas.read_csv('Sat Mar  4 00:58:59 2017')
        data_22 = pandas.read_csv('Sat Mar  4 00:59:53 2017')
        # Select a few portions of the above datafiles that most likely contain little or no specific subvocalization, SV.
        no_sv = data_1[:3000].append([data_1[24000:],data_2[:2000],data_2[19500:],data_3[:2000],data_3[19000:],data_4[:2000],data_4[19000:],data_5[:2000],data_5[18000:],data_6[:1000],data_6[29500:],data_7[:2000],data_7[29000:],data_8[:2000],data_8[26000:],data_9[:2500],data_9[34000:],data_10[:2000],data_10[37000:],data_11[:4000],data_11[25000:],data_12[:2000],data_12[36500:],data_13[:2500],data_13[17500:],data_14[:2500],data_14[23000:],data_15[:2000],data_15[18000:],data_16[:2500],data_16[22500:],data_17[:2000],data_17[27000:],data_18[:2000],data_18[32500:],data_19[:2000],data_19[20000:],data_20[:2000],data_20[33500:],data_21[:2500],data_21[27500:],data_22[:2500],data_22[23000:]],ignore_index=True)
        # Now select a few portions that most likely do contain some specific SV.
        with_sv = data_1[5000:9000].append([data_1[15000:20000],data_2[6000:10000], data_2[12000:18000],data_2[20000:25000],data_3[3000:9000],data_3[12000:14000],data_4[3000:7000],data_4[11000:17000],data_5[2500:10000],data_5[12000:17000],data_6[5500:11000],data_6[12000:21000],data_6[24500:27000],data_7[3000:11000],data_7[14000:19000],data_7[21000:28000],data_8[3000:8000],data_8[11000:15500],data_8[16000:21000],data_8[22000:25500],data_9[3000:9000],data_9[12000:17000],data_9[18000:30000],data_10[7000:14000],data_10[20000:27000],data_10[28000:36000],data_11[5000:7000],data_11[13000:16000],data_11[21000:24000],data_12[3000:15000],data_12[17000:27000],data_12[29000:36000],data_13[3000:17000],data_14[3000:7000],data_14[10000:14000],data_14[17000:21000],data_15[2500:5500],data_15[7500:9000],data_15[12500:17500],data_16[3000:9000],data_16[11000:16000],data_16[17000:22000],data_17[2500:9000],data_17[12000:17000],data_17[19000:26500],data_18[3000:7000],data_18[10000:15000],data_18[17000:19000],data_18[24000:32000],data_19[3000:7000],data_19[9000:15000],data_19[16000:19000],data_20[2500:10000],data_20[15000:23000],data_20[25000:33000],data_21[3000:9000],data_21[10000:16000],data_21[19000:28000],data_22[4000:9000],data_22[11000:15000],data_22[17000:22000]],ignore_index=True)

        return no_sv, with_sv
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
