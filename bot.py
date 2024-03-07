import discord
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
print("Discord Token:", token)

# Define the intents that your bot will use
intents = discord.Intents.default()
intents.messages = True  # For receiving messages
intents.guilds = True    # For guild-related events

# Membuat kelas bot dengan intents
class MyBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        channel = self.get_channel(1107204974452150293)  # Ganti dengan channel ID yang sesuai
        if channel:
            await channel.send('Bot is now online!')  # Pesan yang akan dikirimkan

# Menjalankan bot dengan intents
bot = MyBot(intents=intents)
bot.run(token)