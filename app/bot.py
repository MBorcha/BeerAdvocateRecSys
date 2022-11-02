import telebot
import json
import pandas as pd


bot = telebot.TeleBot("5449612552:AAHW6a1A2OOs1rCgNhjkaD7mprvFB1NcU_4", parse_mode=None)
last_messages = {}
history_by_user = {}
preferences = {}
marks = {}


BASE_OPTIONS_indices = [2093, 412, 1904, 1093, 92, 4083, 276, 88, 7971, 11757]
df = pd.read_csv('../data/beer_reviews.csv')
BASE_OPTIONS = [df.beer_name[df.beer_beerid == x].values[0] for x in BASE_OPTIONS_indices]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    history_by_user[message.from_user.id] = ['start']
    chatid = message.chat.id
    last_messages[message.from_user.id] = message
    bot.reply_to(message, """Привет! Я рекомендую сорта пива на основе твоих предпочтений.""")
    # Вопрос опроса и его ответы.
    questions = "Выбери из списка то, что тебе нравится:"
    answer = BASE_OPTIONS
    # Отправляем опрос в чат
    bot.send_poll(
        chatid, questions, answer,
        is_anonymous=False, allows_multiple_answers=True,
    )


@bot.poll_answer_handler()
def handle_poll_answer(pollAnswer):
    history_by_user[pollAnswer.user.id] = [f'get answers for poll {pollAnswer.poll_id}']
    preferences[pollAnswer.user.id] = [BASE_OPTIONS_indices[i] for i in pollAnswer.options_ids]
    print(pollAnswer)
    print(history_by_user)
    print(preferences)
    give_recommendation(pollAnswer)


def give_recommendation(pollAnswer):
    prefs = preferences[pollAnswer.user.id]

    with open('../model/baseline_output.json', 'r') as f:
        recommendations = json.load(f)

    recs = [recommendations.get(x, None) for x in prefs]
    bot.send_message(last_messages[pollAnswer.user.id].chat.id, f"""Рекомендации: \n(пока не готовы)\n{recs}""")


if __name__ == '__main__':
    bot.infinity_polling()