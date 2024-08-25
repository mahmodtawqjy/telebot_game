import telebot  # Import the telebot library
from telebot import types  # Import the types module
from cachetools import TTLCache  # Import the cachetools library

token = "Put your token here"  # Your bot's token

bot = telebot.TeleBot(token)  # Create an instance of the TeleBot class

# Create a temporary cache for storing data
cache = TTLCache(
    maxsize=20, ttl=100
)  # Set the cache size and time-to-live (in seconds)


@bot.message_handler(
    content_types=[
        "audio",
        "video",
        "document",
        "sticker",
        "voice",
        "location",
        "contact",
        "game",
        "poll",
        "dice",
        "photo",
    ]
)
def content(message):
    bot.reply_to(
        message,
        "Sorry, these file types are not allowed here. Please refrain from sending them. Thank you! ☺️",
    )


@bot.message_handler()
def welcome_message(message):
    c1 = types.BotCommand(
        command="start", description="Click to start the bot"
    )  # Create a command for the user to start the bot
    bot.set_my_commands([c1])  # Set the available commands
    bot.set_chat_menu_button(
        message.chat.id, types.MenuButtonCommands("commands")
    )  # Add the command to the chat menu
    if (
        message.text.lower() != "/start"
    ):  # Check if the user entered a command other than "/start"
        bot.reply_to(message, "Sorry, please use the '/start' command only.")
        return 0
    # Create inline buttons for the initial message
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(
        text="🛠️ Technical Support", url="Put your URL here"
    )
    button2 = types.InlineKeyboardButton(
        text="📣 Telegram Channel", url="Put your URL here"
    )
    button3 = types.InlineKeyboardButton(
        text="😍 Our Services", callback_data="Services"
    )
    button4 = types.InlineKeyboardButton(
        text="💵 Transfer Details", callback_data="details"
    )
    button5 = types.InlineKeyboardButton(text="🤔 About Us", callback_data="about_us")
    button6 = types.InlineKeyboardButton(text="🌐 Social Media", callback_data="media")
    button7 = types.InlineKeyboardButton(text="💵💵 Price List", callback_data="mony")
    # Welcome message
    welcome_text = "Put your text here"
    keyboard.add(button1, button2, button3, button4, button5, button6, button7)
    bot.reply_to(message, welcome_text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.data == "mony":
        mony_message = "Put your text here"
        bot.send_message(call.message.chat.id, mony_message)

    if call.data == "details":
        details_message = "Put your URL here"
        bot.send_message(call.message.chat.id, details_message)

    if call.data == "media":
        keyboard = types.InlineKeyboardMarkup()
        # Social media buttons
        button1 = types.InlineKeyboardButton(text="Facebook", url="Put your URL here")
        button2 = types.InlineKeyboardButton(text="Instagram", url="Put your URL here")
        button3 = types.InlineKeyboardButton(text="YouTube", url="Put your URL here")
        # Add the buttons to the keyboard
        keyboard.add(button1, button2, button3)
        bot.send_message(
            call.message.chat.id,
            "Choose a social media platform:",
            reply_markup=keyboard,
        )

    if call.data == "about_us":
        about_us_message = "Put your text here"
        bot.send_message(call.message.chat.id, about_us_message)

    if call.data == "Services":
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Games", callback_data="games")
        button2 = types.InlineKeyboardButton(
            text="Windows Keys", callback_data="windows_keys"
        )
        keyboard.add(button1, button2)
        bot.send_message(
            call.message.chat.id, "Choose an option:", reply_markup=keyboard
        )
    elif call.data == "win10":
        # Handle Windows 10 option
        bot.send_message(call.message.chat.id, "Put your text here")
    elif call.data == "win11":
        # Handle Windows 11 option
        bot.send_message(call.message.chat.id, "Put your text here")

    if call.data == "games":
        keyboard = types.InlineKeyboardMarkup()
        button_pubg = types.InlineKeyboardButton(text="ببجي", callback_data="pubg")
        keyboard.add(button_pubg)
        bot.send_message(
            call.message.chat.id, "اختر نوع اللعبة:", reply_markup=keyboard
        )
    elif call.data == "pubg":
        keyboard = types.InlineKeyboardMarkup()
        button60 = types.InlineKeyboardButton(text="60 شدة", callback_data="b60")
        button325 = types.InlineKeyboardButton(text="325 شدة", callback_data="b325")
        button660 = types.InlineKeyboardButton(text="660 شدة", callback_data="b660")
        button1800 = types.InlineKeyboardButton(text="1800 شدة", callback_data="b1800")
        button3850 = types.InlineKeyboardButton(text="3850 شدة", callback_data="b3850")
        button8100 = types.InlineKeyboardButton(text="8100 شدة", callback_data="b8100")
        keyboard.add(button60, button325, button660, button1800, button3850, button8100)
        bot.send_message(
            call.message.chat.id,
            "اختر مستوى الشدة:",
            reply_markup=keyboard,
        )
    if call.data == "b60":
        bot.send_message(call.message.chat.id, "Put your text here")
    elif call.data == "b325":
        bot.send_message(call.message.chat.id, "Put your text here")
    elif call.data == "b660":
        bot.send_message(call.message.chat.id, "Put your text here")
    elif call.data == "b1800":
        bot.send_message(call.message.chat.id, "Put your text here")
    elif call.data == "b3850":
        bot.send_message(call.message.chat.id, "Put your text here")
    elif call.data == "b8100":
        bot.send_message(call.message.chat.id, "Put your text here")


bot.infinity_polling()
bot.stop_bot()
