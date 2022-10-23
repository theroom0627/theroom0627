import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == '심장의 부재':
            await message.channel.send('아...심장의 부재...뭐, 간단한겁니다. 심장이 없는 신은 죽은 것이니까요.')
            
        if message.content == '배반자의 정체':
            await message.channel.send('...그건 제가 지금 알려드릴 순 없습니다. 때가 되면 알게 되실껍니다.')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTAzMzY5ODg3MzYxNDU0NDk3Nw.GcrGht.S6xUksmqCy8vt9gEopE6mlJzUjBQGDMsez1Tb0')