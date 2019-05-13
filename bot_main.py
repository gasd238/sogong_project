import asyncio
import discord
import re
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
        embed, save_stat = check_opt(msg)

        if save_stat == 0 or save_stat == -1:
            await client.send_message(message.channel, embed = embed)

        elif save_stat == 1:
            embed = discord.Embed(title='추가하기', description='저장할 id, 비밀번호와 그것의 사이트를 입력해 주세요')
            embed.add_field(name = '예시', value = '옥션 abcd1234 1234567')
            await client.send_message(message.channel, embed = embed)
            response = await client.wait_for_message(timeout=float(15), author=message.author, channel=message.channel)

            if response == None:
                await client.send_message(message.channel, '제대로 입력하지 않았습니다. 다시 시도해 주세요')
                return
            
            content = response.content.split(' ')
            hangul = re.compile('[ㄱ-ㅣ가-힣]+')
            if len(content) != 3 or hangul.findall(content[1]) != [] or hangul.findall(content[2]) != []:
                await client.send_message(response.channel, '제대로 입력하지 않았습니다. 다시 시도해 주세요')

            else:
                info_add(content, response.author.id)
        
        elif save_stat == 2:
            embed = discord.Embed(title='삭제하기', description='삭제할 정보의 사이트를 입력해 주세요')
            

                

        

client.run('token')
