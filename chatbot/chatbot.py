from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot= ChatBot("BotBoy")
 
corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train("chatterbot.corpus.english")

convo=[
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

trainer= ListTrainer(bot)
trainer.train(convo)

while True:
    question=input()

    if question=='x':
        break
    answer=bot.get_response(question)
    print(answer)
