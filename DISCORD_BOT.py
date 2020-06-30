import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트중입니다.")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("!welcome"):
        await message.channel.send(" 어서오세요~"
                                   "처음 오셨다면 #💬자기소개_양식 채널을 확인해주세요!"
                                   "확인 하셨다면, 양식에 맞추어서 #💬자기소개 를 기록해주세요!"
                                   "자기소개를 마치신 후에 안내를 받으실 준비가 되었다면   @안내팀 [Newbie Manager]    을 불러주세요!!"
                                   " 서버 이용과 관련된 사항을 안내해 드린 뒤 정식유저 권한을 드려요!! **  ")



client.run("NzE4MzExMDA5ODAyMTI1MzUy.Xvk0mw.k5wqm1kCSnRuK0HctSEw8GsUo38")
