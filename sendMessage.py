import asyncio
import telegram
from decouple import config

# Replace <bot_token> with your actual bot token
token = config('TOKEN')
bot = telegram.Bot(token)

async def send_message(chat_id, text):
    await bot.send_message(chat_id, text)

# Replace <chat_id> with the actual chat ID
chat_id = config('CHAT_ID')

# Replace 'Test Message' with the actual message you want to send
text = 'Test Message'

# Call the send_message coroutine and await the result
asyncio.run(send_message(chat_id, text))