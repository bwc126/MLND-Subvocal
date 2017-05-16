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
