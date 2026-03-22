import discord
import os

TOKEN = os.getenv("TOKEN")
SOURCE_CHANNEL_ID = int(os.getenv("SOURCE_CHANNEL_ID"))
TARGET_CHANNEL_ID = int(os.getenv("TARGET_CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.channel.id != SOURCE_CHANNEL_ID:
        return

    if message.author.bot:
        return

    target_channel = client.get_channel(TARGET_CHANNEL_ID)

    if target_channel:
        content = f"**{message.author.name}:** {message.content}"

        # Forward attachments
        if message.attachments:
            content += "\n" + "\n".join([a.url for a in message.attachments])

        await target_channel.send(content)

client.run(TOKEN)