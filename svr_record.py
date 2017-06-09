from tkinter import *
from pcf8591read import *
import threading

root = Tk()

def testytesty():
    print ('oh look we used a callback')
# words from https://www.randomlists.com/random-words


# reader_worker = reader.run

class svr_interface():
    def __init__(self):
        self.current = 0
        self.words = ['dusty','march','direful','complete','superb','poised','wait','quaint','save','copy','interest','separate','bright','utter','bored','nondescript','license','vest','dance','money','languid','swim','enthusiastic','quartz','planes','spiritual','imperfect','coal','hobbies','sound','bow','squirrel','push','treatment','mine','precede','weather','amazing','round','stingy','signal','marry','country','uncle','dust','certain','loose','knock','advice','confuse','animated','loving','feeling','absorbing','trick','spare','rod','caption','raspy','throne','clumsy','vague','tow','hang','rely','tired','barbarous','pan','innocent','combative','low','rub','mixed','actually','faulty','thirsty','dam','doubtful','flowers','defective','frogs','outstanding','ducks','icicle','fry','load','cracker','efficient','hop','fax','fancy','reading','real','addicted','motion','clean','unsuitable','race','aspiring','gold','check','bouncy','regret','chop','various','eminent','wander','living','equable','cluttered','geese','tightfisted','aftermath','quince','division','board','amuck','pretty','extra-large','sun','person','magical','invent','flap','stomach','black','river','town','type','stereotyped','paddle','expand','puncture','cakes','measly','kitty','courageous','shoe','number','third','ugliest','haircut','increase','wrathful','jog','straw','whisper','kick','talented','curious']
        self.reader = adc_reader()
        self.suffix = 0
        self.current_word = self.words[self.current]
        self.filename = self.current_word + '-' + str(self.suffix)
        self.r_t = threading.Thread(target=self.reader.run,args=[self.filename])
        self.r_t.daemon = True

        def key(event):
            print ("pressed", repr(event.char))
            # current_word = self.words[self.current]
            # filename = current_word + '-' + str(suffix)
            if event.char.isdigit():
                suffix = event.char
                print ('file series will take',suffix,'as suffix in filename')
            if event.char==' ':
                print('starting thread')
                print(self.current_word)
                self.reader.record = True
                # Get the next word
                # Start the recording for that word
                # reader.run(filename)
                # r_t.run([filename])
                # self.r_t.start()
            # If the recording is running:
            if event.char=='s':
                self.reader.record = False
                # Stop the recording
                self.current += 1
                print('terminating thread',self.current)
                # print('r_t:',vars(self.r_t),'r_t._target:',vars(self.r_t._target))

                # Iterate the word



        def callback(event):
            frame.focus_set()
            print ("clicked at", event.x, event.y)

        frame = Frame(root, width=100, height=100)
        frame.current = 0
        frame.bind("<Key>", key)
        frame.bind("<Button-1>", callback)
        frame.pack()

        root.mainloop()

s_inter = svr_interface()
