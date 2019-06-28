import discord
import asyncio
from itertools import cycle

client = discord.Client()

statusmsg = ['namu!help를 입력하세요!','나무봇 개발중!']

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

async def change_status():
    await client.wait_until_ready()
    messages = cycle(statusmsg)

    while not client.is_closed():
        current_status = next(messages)
        game = discord.Game(current_status)
        await client.change_presence(status=discord.Status.online,activity=game)
        await asyncio.sleep(4)

@client.event
async def on_message(message):
    if message.content.startswith("namu!help"):
        try:
            embed = discord.Embed(title="도움말",description="나무봇 도움말 입니다.",colour=discord.Color.green())

            embed.add_field(name="명령어",value="namu!help\nnamu!hi\nnamu!status\nnamu!beep")
            await message.channel.send(embed=embed)
        except discord.errors.Forbidden:
            await message.channel.send("```ForBidden 오류가 났습니다. (오류 원인 예상: 링크 첨부 권한 이 없는것 같습니다. 봇에게 링크첨부 권한을 추가해 주세요.)\n대신 텍스트로 대체합니다.```\n\n명령어:\n```namu!help\nnamu!hi\nnamu!status\nnamu!beep```") 
    if message.content.startswith("namu!hi"):
        await message.channel.send("네 안녕하세요~~~")
    if message.content.startswith("namu!status"):
        ping = client.latency
        await message.channel.send("봇의 핑: " + str(ping) + "s")
    if message.content.startswith("namu!beep"):
        await message.channel.send("boooooop!")
    if message.content.startswith("namu!87ab392399c84109ac9550f301c48450"):
        await message.channel.send("공지 테스트 입니다")

client.loop.create_task(change_status())
client.run("NTg5Njk5MDE0MzU4ODU5Nzg2.XRX7Vg.S1nxRN0QsL2Q9cEBTvN3SsmE1AM")