# Импорт необходимых библиотек
import telebot  # Библиотека для работы с Telegram Bot
from telebot import types  # Импорт типов данных из библиотеки telebot
import sqlite3  # Библиотека для работы с SQLite базой данных
import os  # Библиотека для работы с операционной системой

# Создание экземпляра бота с токеном для доступа к Telegram Bot
bot = telebot.TeleBot("7365269398:AAF6F49NOoo8WB_MeQL97zgBbfX1isYIba4")

# Создание кнопок для регистрации и авторизации
button = types.InlineKeyboardButton(text="REGISTRATION", callback_data="registration")
button2 = types.InlineKeyboardButton(text="AUTHORIZATION", callback_data="authorization")
# Создание клавиатуры с кнопками
keyboard = types.InlineKeyboardMarkup(keyboard=[[button, button2]])

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Отправка сообщения пользователю с предложением зарегистрироваться или авторизоваться и прикрепленной клавиатурой
    bot.send_message(
        message.chat.id, 
        'Hello! You are a new user? Please register, if not, please authorize.', 
        reply_markup=keyboard
    )

# Словарь для временного хранения данных пользователей
user_data = {}

# Обработчик нажатий на кнопки
@bot.callback_query_handler(lambda callback: True)
def callback_handler(callback):
    # Если нажата кнопка "REGISTRATION"
    if callback.data == 'registration':
        # Запрос логина для регистрации
        bot.send_message(callback.message.chat.id, 'Please enter your login:')
        # Переход к следующему шагу - обработке логина
        bot.register_next_step_handler(callback.message, process_login_step)
    # Если нажата кнопка "AUTHORIZATION"
    elif callback.data == 'authorization':
        # Запрос логина или email для авторизации
        bot.send_message(callback.message.chat.id, 'Please enter your login or email:')
        # Переход к следующему шагу - обработке логина или email для авторизации
        bot.register_next_step_handler(callback.message, process_auth_login_step)

# Обработка ввода логина при регистрации
def process_login_step(message):
    chat_id = message.chat.id
    # Сохранение введенного логина в словаре user_data
    user_data[chat_id] = {'login': message.text}
    # Запрос email
    bot.send_message(chat_id, 'Please enter your email:')
    # Переход к следующему шагу - обработке email
    bot.register_next_step_handler(message, process_email_step)

# Обработка ввода email при регистрации
def process_email_step(message):
    chat_id = message.chat.id
    # Сохранение введенного email в словаре user_data
    user_data[chat_id]['email'] = message.text
    # Запрос пароля
    bot.send_message(chat_id, 'Please enter your password:')
    # Переход к следующему шагу - обработке пароля
    bot.register_next_step_handler(message, process_password_step)

# Обработка ввода пароля при регистрации
def process_password_step(message):
    chat_id = message.chat.id
    # Сохранение введенного пароля в словаре user_data
    user_data[chat_id]['password'] = message.text
    # Запрос подтверждения пароля
    bot.send_message(chat_id, 'Please confirm your password:')
    # Переход к следующему шагу - обработке подтверждения пароля
    bot.register_next_step_handler(message, process_password_confirmation_step)

# Обработка подтверждения пароля при регистрации
def process_password_confirmation_step(message):
    chat_id = message.chat.id
    password = user_data[chat_id]['password']
    password_confirmation = message.text

    # Проверка совпадения пароля и его подтверждения
    if password == password_confirmation:
        bot.send_message(chat_id, 'Registration successful!')
        # Сохранение данных пользователя в базу данных
        save_user_to_database(chat_id)
    else:
        bot.send_message(chat_id, 'Passwords do not match. Please try again.')
        # Повторный запрос пароля в случае несовпадения
        bot.send_message(chat_id, 'Please enter your password:')
        bot.register_next_step_handler(message, process_password_step)

# Сохранение данных пользователя в базу данных
def save_user_to_database(chat_id):
    data = user_data[chat_id]
    # Получение абсолютного пути к базе данных
    database_path = os.path.abspath(os.path.join(__file__, '../../shop/data.db'))
    # Подключение к базе данных SQLite
    database = sqlite3.connect(database_path)
    cursor = database.cursor()
    
    # Вставка данных пользователя в таблицу user
    cursor.execute('INSERT INTO user (login, email, password) VALUES (?, ?, ?)', 
                   (data['login'], data['email'], data['password']))
    database.commit()  # Сохранение изменений в базе данных
    database.close()  # Закрытие соединения с базой данных

    # Уведомление пользователя о успешном сохранении данных
    bot.send_message(chat_id, 'Your registration data has been saved successfully.')

    # Удаление данных пользователя из временного хранилища
    del user_data[chat_id]

# Обработка ввода логина или email при авторизации
def process_auth_login_step(message):
    chat_id = message.chat.id
    # Сохранение введенного логина или email в словаре user_data
    user_data[chat_id] = {'auth_login': message.text}
    # Запрос пароля
    bot.send_message(chat_id, 'Please enter your password:')
    # Переход к следующему шагу - обработке пароля для авторизации
    bot.register_next_step_handler(message, process_auth_password_step)

# Обработка ввода пароля при авторизации
def process_auth_password_step(message):
    chat_id = message.chat.id
    # Сохранение введенного пароля в словаре user_data
    user_data[chat_id]['auth_password'] = message.text
    # Проверка пользователя в базе данных
    check_user_in_database(chat_id)

# Проверка наличия пользователя в базе данных
def check_user_in_database(chat_id):
    data = user_data[chat_id]
    # Получение абсолютного пути к базе данных
    database_path = os.path.abspath(os.path.join(__file__, '../../shop/data.db'))
    # Подключение к базе данных SQLite
    database = sqlite3.connect(database_path)
    cursor = database.cursor()
    
    # Запрос пользователя по логину или email и паролю
    cursor.execute('SELECT * FROM user WHERE (login=? OR email=?) AND password=?', 
                   (data['auth_login'], data['auth_login'], data['auth_password']))
    user = cursor.fetchone()  # Получение результата запроса
    database.close()  # Закрытие соединения с базой данных

    if user:
        # Проверка, является ли пользователь администратором
        is_admin = user[5]  # Предполагается, что 6-е поле в таблице - это статус администратора
        if is_admin == 1:
            # Если пользователь администратор, отправляется соответствующее сообщение
            bot.send_message(chat_id, 'Hey, you are an administrator! This is our site and you can change it - http://127.0.0.1:5000')
        else:
            # Если пользователь не администратор, отправляется сообщение о успешной авторизации
            bot.send_message(chat_id, 'Authorization successful! Please visit our website - http://127.0.0.1:5000!')
    else:
        # Если данные не найдены, отправляется сообщение о неудачной авторизации
        bot.send_message(chat_id, 'Authorization failed. Please check your login/email and password.')

    # Удаление данных пользователя из временного хранилища
    del user_data[chat_id]

# Запуск бесконечного опроса бота, чтобы бот постоянно проверял наличие новых сообщений
bot.infinity_polling()
