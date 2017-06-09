import pcf8591read

reader = pcf8591read.adc_reader()
filename = input('Current word:')
reader.record = True
reader.run(filename)
