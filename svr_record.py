from tkinter import *
from pcf8591read import *
import threading

root = Tk()

def testytesty():
    print ('oh look we used a callback')
# words from https://www.randomlists.com/random-words
words = ['dusty','march','direful','complete','superb','poised','wait','quaint','save','copy','interest','separate','bright','utter','bored','nondescript','license','vest','dance','money','languid','swim','enthusiastic','quartz','planes','spiritual','imperfect','coal','hobbies','sound','bow','squirrel','push','treatment','mine','precede','weather','amazing','round','stingy','signal','marry','country','uncle','dust','certain','loose','knock','advice','confuse','animated','loving','feeling','absorbing','trick','spare','rod','caption','raspy','throne','clumsy','vague','tow','hang','rely','tired','barbarous','pan','innocent','combative','low','rub','mixed','actually','faulty','thirsty','dam','doubtful','flowers','defective','frogs','outstanding','ducks','icicle','fry','load','cracker','efficient','hop','fax','fancy','reading','real','addicted','motion','clean','unsuitable','race','aspiring','gold','check','bouncy','regret','chop','various','eminent','wander','living','equable','cluttered','geese','tightfisted','aftermath','quince','division','board','amuck','pretty','extra-large','sun','person','magical','invent','flap','stomach','black','river','town','type','stereotyped','paddle','expand','puncture','cakes','measly','kitty','courageous','shoe','number','third','ugliest','haircut','increase','wrathful','jog','straw','whisper','kick','talented','curious']


reader = adc_reader()
# reader_worker = reader.run


def key(event):
    current = 0
    print ("pressed", repr(event.char))
    suffix = 0
    current_word = words[current]
    filename = current_word + '-' + str(suffix)
    r_t = threading.Thread(target=reader.run,args=[filename])
    if event.char.isdigit():
        suffix = event.char
        print ('file series will take',suffix,'as suffix in filename')
    if event.char==' ':
        # If the recording is running:
        if r_t.is_alive():
            print('terminating thread')
            reader.record = False
            # Stop the recording
            current += 1
            # Iterate the word
        else:
            print('starting thread')
            reader.record = True
            # Get the next word
            # Start the recording for that word
            print(current_word)
            # reader.run(filename)
            # r_t.run([filename])
            r_t.daemon = True
            r_t.start()



def callback(event):
    frame.focus_set()
    print ("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
