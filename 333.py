import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

# 机器人的 API 令牌
bot_token = '6867402496:AAFEfZUD-KANCVl0fGtZccRtEFLMqao_DCE'

# 初始化 Telegram Bot
bot = telegram.Bot(token=bot_token)

# 定义启动命令处理程序
def start(update, context):
    user = update.effective_user
    keyboard = [
        [InlineKeyboardButton("按钮1", callback_data='button1')],
        [InlineKeyboardButton("按钮2", callback_data='button2')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        f"你好，{user.mention_markdown_v2()}！",
        reply_markup=reply_markup
    )

# 定义按钮回调处理程序
def button(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"你选择了按钮: {query.data}")

# 定义文本消息处理程序
def echo(update, context):
    update.message.reply_text(update.message.text)

# 创建 Updater 和添加处理程序
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(button))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# 启动机器人
updater.start_polling()
updater.idle()
