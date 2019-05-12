import asyncio
import discord
from module.help import *
from module.check import *
from module.save import *

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------------------')
    await client.change_presence(game=discord.Game(name="sj help로 도움말", type=0))
@client.event
async def on_message(message):
    #명령어 출력관련
    if message.content == 'sj help':
        await client.send_message(message.channel, embed = help())
    if message.content.startswith('sj save'):
        msg = message.content.split(' ')
        embed, save_stat = check_opt(msg, message.author.id)
        if save_stat == 0 or save_stat == -1:
            await client.send_message(message.channel, embed = embed)
        elif save_stat == 1:
            embed = discord.Embed(title='추가하기', description='저장할 id, 비밀번호와 그것의 사이트를 입력해 주세요')
            embed.add_field(name = '예시', value = '옥션 abcd1234 1234567')
            await client.send_message(message.channel, embed = embed)
            response = await client.wait_for_message(timeout=float(30), author=message.author, channel=message.channel)

            if response == None:
                await client.send_message(message.channel, '제대로 입력하지 않았습니다. 다시 시도해 주세요')
                return

                

        

client.run('NTY5NzY4NjgzMjMzMzQ1NTM3.XMaP5w.lwEMG--Bvq8IyXkkUjKOJcONj5g')