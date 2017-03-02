import csv

def create_file(filename):
    with open(filename, 'w') as csvfile:
        fieldnames = ['time', 'voltage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

def write_file(filename, time, voltage):
    with open(filename, 'w') as csvfile:
        fieldnames = ['time', 'voltage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'time': time, 'voltage': voltage})
