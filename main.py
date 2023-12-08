import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)      #Создается клавиатура для ответа, которая будет содержать кнопки для выбора ответов. Она настраивается на автоматическое изменение размера.
    item1 = types.KeyboardButton("🌟 Начнем 🌟")

    markup.add(item1)
    bot.send_message(message.chat.id,
                     f"Добро пожаловать, {message.from_user.first_name}!\nЯ - <b>{bot.get_me().first_name}</b>. Готов начать викторину❓",
                     parse_mode='html', reply_markup=markup)
#parse_mode='html', чтобы обеспечить разметку HTML в сообщении, и reply_markup=markup для добавления созданной клавиатуры ответа.

# Словарь с вопросами и правильными ответами для викторины(последний)
quiz = {
    "Как называется столица Франции?": ["Марсель", "Лион", "Ницца", "Париж", "Париж"],
    "Как называется самая большая планета в Солнечной системе?": ["Марс", "Юпитер", "Венера", "Сатурн", "Юпитер"],
    "Кто написал произведение 'Преступление и наказание'?": ["Лев Толстой", "Иван Тургенев", "Федор Достоевский",
                                                             "Антон Чехов", "Федор Достоевский"],
    "Какой химический элемент обозначается символом 'Fe'?": ["Железо", "Фтор", "Фосфор", "Франций", "Железо"],
    "Какой год считается началом Великой Отечественной войны?": ["1941", "1942", "1943", "1944", "1941"],
    "Какой город является столицей Японии?": ["Осака", "Киото", "Саппоро", "Токио", "Токио"],
    "Какое животное является символом года 2023 по китайскому календарю?": ["Змея", "Крыса", "Коза", "Тигр", "Тигр"],
    "Как называется самая длинная река в мире?": ["Миссисипи", "Нил", "Амазонка", "Волга", "Амазонка"],
    "Какое событие начало Первую мировую войну?": ["Убийство Франца Фердинанда", "Взрыв Луситании",
                                                   "Подписание Брест-Литовского мира",
                                                   "Подписание Версальского договора", "Убийство Франца Фердинанда"],
    "Как называется единица измерения силы землетрясения?": ["Вольт", "Ватт", "Рихтер", "Фарад", "Рихтер"]
}

current_question = None  # Текущий вопрос
user_answers = {}  # Словарь для хранения ответов пользователя
answered_question_count = 0  # Количество отвеченных вопросов

@bot.message_handler(func=lambda message: message.text == '🌟 Начнем 🌟' and message.chat.type == 'private' or message.text == '🌟 Начнем заново 🌟')
def start_quiz(message):
    global user_answers, answered_question_count
    user_answers = {}
    answered_question_count = 0
    ask_question(message)

def ask_question(message):
    global current_question   #текущий вопрос
    available_questions = list(set(quiz.keys()) - set(user_answers.keys()))    #доступный вопрос:определяется на какой вопрос еще не ответили

    if answered_question_count == 5:  # Лимит вопросов установлен на 5
        show_results(message)
        return

    if not available_questions:
        show_results(message)
        return

    current_question = random.choice(available_questions)

    # Отправка вопроса с вариантами ответов
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answers = quiz[current_question][:4]
    random.shuffle(answers)
    for answer in answers:
        markup.add(types.KeyboardButton(answer))

    bot.send_message(message.chat.id, f"{current_question}?", reply_markup=markup)  #отправка сообщения

@bot.message_handler(func=lambda message: message.text in quiz[current_question] if current_question else False)  #содержится ли текст сообщения пользователя в списке вариантов ответа на текущий вопрос (message.text in quiz[current_question]). Если current_question не определен (равен None), возвращается False
def handle_answer(message):
    global current_question, answered_question_count
    if current_question is not None:
        user_answers[current_question] = message.text
        answered_question_count += 1
        ask_question(message)     #задать следующий вопрос
    else:
        bot.send_message(message.chat.id, "Чтобы начать викторину, используйте команду /start")

@bot.message_handler(commands=['end_quiz'])
def end_quiz(message):
    show_results(message)

def show_results(message):
    correct_answers = 0
    wrong_answers = []

    for question, user_answer in user_answers.items():
        correct_answer = quiz[question][-1]     #правильный ответ
        if user_answer == correct_answer:
            correct_answers += 1
        else:
            wrong_answers.append(f"Вопрос: {question}\nВаш ответ: {user_answer}\nПравильный ответ: {correct_answer}\n")

    answered_questions = len(user_answers)     #количество оветов
    result_message = f"Правильных ответов: {correct_answers} из {answered_questions}\n\n"
    if wrong_answers:
        result_message += "Неправильные ответы:\n\n" + "\n".join(wrong_answers)
    else:
        result_message += "Все ответы верны!"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🌟 Начнем заново 🌟")
    markup.add(item1)
    bot.send_message(message.chat.id, result_message, reply_markup=markup)

# запуск
bot.polling(none_stop=True)
