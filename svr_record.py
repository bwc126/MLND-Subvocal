from tkinter import *
from pcf8591read import *

root = Tk()

def testytesty():
    print ('oh look we used a callback')
# words from https://www.randomlists.com/random-words
words = ['dusty','march','direful','complete','superb','poised','wait','quaint','save','copy','interest','separate','bright','utter','bored','nondescript','license','vest','dance','money','languid','swim','enthusiastic','quartz','planes','spiritual','imperfect','coal','hobbies','sound','bow','squirrel','push','treatment','mine','precede','weather','amazing','round','stingy','signal','marry','country','uncle','dust','certain','loose','knock','advice','confuse','animated','loving','feeling','absorbing','trick','spare','rod','caption','raspy','throne','clumsy','vague','tow','hang','rely','tired','barbarous','pan','innocent','combative','low','rub','mixed','actually','faulty','thirsty','dam','doubtful','flowers','defective','frogs','outstanding','ducks','icicle','fry','load','cracker','efficient','hop','fax','fancy','reading','real','addicted','motion','clean','unsuitable','race','aspiring','gold','check','bouncy','regret','chop','various','eminent','wander','living','equable','cluttered','geese','tightfisted','aftermath','quince','division','board','amuck','pretty','extra-large','sun','person','magical','invent','flap','stomach','black','river','town','type','stereotyped','paddle','expand','puncture','cakes','measly','kitty','courageous','shoe','number','third','ugliest','haircut','increase','wrathful','jog','straw','whisper','kick','talented','curious']

current = 0

reader = adc_reader()

def key(event):
    print ("pressed", repr(event.char))
    if event.char.isdigit():
        suffix = event.char
        print ('file series will take',suffix,'as suffix in filename')
    if event.char==' ':
        if reader.record == False:
            # Get the next word
            current_word = words[current]
            # Start the recording for that word
            print(current_word)
            filename = current_word + suffix
            reader.run(filename)

        # If the recording is running:
        if reader.record:
            reader.record = False
            # Stop the recording
            current += 1
            # Iterate the word


def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
