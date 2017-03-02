#! /usr/bin/env python3

import sys, time
from time import sleep
from quick2wire.parts.pcf8591 import *
from quick2wire.i2c import I2CMaster
#from vis import volt_plot
from writefile import *
from tkinter import *

address = int(sys.argv[1]) if len(sys.argv) > 1 else BASE_ADDRESS
pin_index1 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
pin_index2 = int(sys.argv[3]) if len(sys.argv) > 3 else 1
create_file('test')
root = Tk()
subvocal = ''

def key(event):
  if event.char == 'a':
    subvocal = 'Y'
    voltage = pin1.value * 3.3
    print("read: {} : {}".format(count, voltage))
    current = time.clock() - start
    write_file('test', current, voltage, subvocal)
  else:
    subvocal = "N"
    voltage = pin1.value * 3.3
    print("read: {} : {}".format(count, voltage))
    current = time.clock() - start
    write_file('test', current, voltage, subvocal)

with I2CMaster() as i2c:
    adc = PCF8591(i2c, THREE_DIFFERENTIAL)
    pin1 = adc.differential_input(1)
    #pin2 = adc.single_ended_input(pin_index2)

    count = 1
    #data = {}
    start = time.clock()

    frame = Frame(root, width=100, height=100)
    frame.bind("<Key>", key)
    frame.pack()
    root.mainloop()


    # while True:
    #     voltage = pin1.value * 3.3
    #     print("read: {} : {}".format(count, voltage))
    #     #sleep(0.1)
    #     count += 1
    #     current = time.clock() - start
    #
    #     write_file('test', current, voltage, )
    #     #data[count] = pin1.raw_value
    #     #volt_plot(count, data)
