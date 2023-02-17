import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai

openai.api_key = "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"


# Define the handler function for the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hi! I'm a Chant GPT bot. Send me a message and I'll generate some text for you.")


# Define the handler function for text messages
def generate_text(update, context):
    # Get the text message from the user
    text = update.message.text

    # Use the Chant GPT model to generate a response
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Send the generated response back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

TOKEN = "6000271669:AAHH6HdPI9wap_dr2HNSl4mqNNrYbwvaips"
# Set up the Telegram bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Set up the command and message handlers
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

text_handler = MessageHandler(Filters.text & ~Filters.command, generate_text)
dispatcher.add_handler(text_handler)

# Start the bot
updater.start_polling()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
