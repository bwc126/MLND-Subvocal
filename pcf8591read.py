#! /usr/bin/env python3

import sys, time
from time import sleep
from quick2wire.parts.pcf8591 import *
from quick2wire.i2c import I2CMaster
#from vis import volt_plot
from writefile import *
from tkinter import *

class adc_reader():

    def __init__(self):

        self.address = int(sys.argv[1]) if len(sys.argv) > 1 else BASE_ADDRESS
        self.pin_index1 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
        self.pin_index2 = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        self.record = False



    def run(self, filename):
        with I2CMaster() as i2c:
            adc = PCF8591(i2c, THREE_DIFFERENTIAL)
            pin1 = adc.differential_input(1)

            #pin2 = adc.single_ended_input(pin_index2)
            # root = Tk()
            # def key(event):
            #     print(event.char)
            #     if event.char == 'a':
            #         subvocal = 'Y'
            #         voltage = pin1.value * 3.3
            #         print("read: {} : {}".format(count, voltage))
            #         current = time.clock() - start
            #         write_file('test.csv', current, voltage, subvocal)
            #     else:
            #         subvocal = "N"
            #         voltage = pin1.value * 3.3
            #         print("read: {} : {}".format(count, voltage))
            #         current = time.clock() - start
            #         write_file('test.csv', current, voltage, subvocal)

            # frame = Frame(root, width=300, height=300)
            # frame.bind("<Key>", key)
            # frame.pack()
            # root.mainloop()
            #data = {}
            count = 0
            start = time.clock()

            with open(filename, 'w') as csvfile:

                fieldnames = ['time', 'count', 'voltage']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                count = 1
                while self.record:
                    reading = ''
                    voltage = pin1.value * 3.3
                    strength = ['-' for i in range(int(pin1.value//16))]
                    reading += str([bar for bar in strength])
                    print (reading)
                    #sleep(0.1)
                    count += 1
                    current = time.clock() - start
                    #data[count] = pin1.raw_value
                    #volt_plot(count, data)
                    writer.writerow({'time': current, 'count': count, 'voltage': voltage})
