from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer



bot = ChatBot("QA")

trainer = ListTrainer(bot)


trainer.train(['hello', 'hey', 'how are you?', 'I am fine, thank you', 'how about you?', 'I am good, thanks', 'how can I help you?', 'I need to learn English'])


response = bot.get_response(input("Type something..."))




if __name__ == '__main__':
	print(response)
