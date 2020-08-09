from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *
import threading
import pyttsx3 as pt
import speech_recognition as s


engine= pt.init()#intstantiate audio  engine
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[1].id)



def speak(word):
    engine.say(word)
    engine.runAndWait()




bot = ChatBot("BotBoy")


convo = [
    'hello',
    'hi!!',
    'how are you?!',
    'i am fine',
    'what is your name?',
    "my name is BotBoy",
    'who created you',
    'I was created by akshay',
    'lets dance!',
    'ok!!'
]

trainer = ListTrainer(bot)
trainer.train(convo)


main= Tk()
main.geometry("500x600")
main.title("BotBoy")
#imag=PhotoImage(file="OIP.png")
#plabel=Label(main,image=imag)
#plabel.pack(pady=5 )

def takequery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("yput bot is litsenig")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textfield.delete(0, END)
            textfield.insert(0, query)
            askfrombot()

        except  Exception as e:
            print(e)
            print("not recofnised")



def askfrombot():
        print("clicked")


        query = textfield.get()

        if query == 'x':
            exit(0)


        answer=bot.get_response((query))
        msg.insert(END,"ME: "+query)

        msg.insert(END,"BotBoy: "+str(answer))
        speak(answer)
        textfield.delete(0, END)
        msg.yview(END)


frame=Frame(main)
scbar=Scrollbar(frame)
msg=Listbox(frame,width=80,height=20, yscrollcommand=scbar.set)
scbar.pack(side=RIGHT,fill=Y)
msg.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

textfield=Entry(main,font=("vVerdana",20))
textfield.pack(fill=X,pady=10)

ask=Button(main, text="ASK BOT A QUESTION : ",font=("Verdana,20"),command=askfrombot)
ask.pack()

def enterfnct(event):
    ask.invoke()






main.bind('<Return>',enterfnct)


def repeat():
    while True:
        takequery()

t=threading.Thread(target=repeat)
t.start()

main.mainloop()