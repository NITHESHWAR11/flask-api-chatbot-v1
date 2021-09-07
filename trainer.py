from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk

 nltk.download()
bot = ChatBot('Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3')

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    './data'
        )
def response(user_input):
        response1 = bot.get_response(user_input)
        return response1
