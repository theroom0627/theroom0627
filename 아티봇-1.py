import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == '안녕?':
            await message.channel.send('안녕하세요 여러분! 전 아티라고 합니다! 여러분을 모시러온 접객원이죠!')

        if message.content == '여긴 왜 왔어?':
            await message.channel.send('음...여긴 대화하기 적절하지 않은 것 같은데...다른 곳으로 가죠!')
        
        if message.content == '반가워!':
            await message.channel.send('저도 반가워요!')

        if message.content == '띵동':
            await message.channel.send('여긴 프론트가 아니랍니다?')

        if message.content == '혹시 술은 없어?':
            await message.channel.send('음...일단 여긴 호텔이 아니고요! 저희 호텔에서도 술을 제공하지 않습니다')
        
        if message.content == '주소는?':
            await message.channel.send('FRsMBuEcxX')

        if message.content == '심장의 부재':
            await message.channel.send('아...심장의 부재...뭐, 간단한겁니다. 심장이 없는 신은 죽은 것이니까요.')
            
        if message.content == '배반자의 정체':
            await message.channel.send('...그건 제가 지금 알려드릴 순 없습니다. 때가 되면 알게 되실껍니다.')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTAzMzY5ODg3MzYxNDU0NDk3Nw.Gr8m89.xDiHG7zgRH9lGzRlQ8tTHodMs60ceNhHhXjw3M')