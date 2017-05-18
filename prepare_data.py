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
        # Select a few portions of the above datafiles that most likely contain little or no specific subvocalization, SV.
        no_sv = data_1[:3000].append(data_2[:2000]).append(data_3[:2000]).append(data_4[:2000]).append(data_5[:2000])
        # Now select a few portions that most likely do contain some specific SV.
        with_sv = data_1[5000:9000].append(data_2[6000:10000]).append(data_3[3000:9000])
        
        return no_sv, with_sv
