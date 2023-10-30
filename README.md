from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# 替换为您的机器人API令牌
bot_token = '6867402496:AAFEfZUD-KANCVl0fGtZccRtEFLMqao_DCE'

# 处理/start命令
def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    update.message.reply_text(f'欢迎，您的用户ID是 {user_id}。')

# 处理用户消息
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = generate_response(user_message)
    update.message.reply_text(response)

# 生成聊天回应（示例中的简单回应）
def generate_response(user_message):
    # 在这里可以编写根据用户消息生成回应的逻辑
    if "你好" in user_message:
        return "你好！"
    else:
        return "谢谢您的消息。"

def main():
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

飞机
