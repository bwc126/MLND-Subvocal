import pcf8591read

reader = adc_reader()
filename = input('Current word:')
reader.record = True
reader.run(filename)
