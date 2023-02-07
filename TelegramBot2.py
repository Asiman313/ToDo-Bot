import telebot
import random
token = "6084446354:AAEaYJlJtGQMJs2fIIJnZTFpv-ZGawQApDE"
bot = telebot.TeleBot(token)
HELP = """
/help - Вывести справку по программе.
/add - Добавить задачу в споисок.
/show -  Напечатать все добавленные задачи.
/random - случайная задача из списка на сегодня.
"""
tasks = {

}
random_1 = ("Отжаться 5 раз", "Совершить 20 минутную прогулку", "Приготовить интересное блюдо", "Поиграть на гитаре")

def my_date(date,task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "<b>Привет! Это ToDo бот. Я второй проект Асимана по созданию телеграм канала :)</b>", parse_mode="html")

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    text = ("Отлично! Задача " + task + " добавлена в список на дату " + date)
    my_date(date, task)
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
        task = random.choice(random_1)
        date = "cегодня"
        my_date(date, task)
        text = "Случайная задача на " + date + " - " + task
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show"])
def show_1(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper()
        for task in tasks[date]:
            text = "Задачи на " + text + " - " + task
    else:
        text = "Задач на " + date + " нет"
    bot.send_message(message.chat.id, text)

bot.polling(none_stop = True)

