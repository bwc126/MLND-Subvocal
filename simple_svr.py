import pcf8591read
"""
This is a barebones script for controlling the work flow of recording EMG words and associating the data with a specific word, captured in the filename.
"""
reader = pcf8591read.adc_reader()
filename = input('Current word:')
reader.record = True
reader.run(filename)
