import asyncio
import discord
import re
from module.help import *
from module.check import *
from module.save import *
from module.simsim import *

client = discord.Client()
#심심이 플레이 상태 확인용 
stat_chk = [0]

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
            mudel = await client.send_message(message.channel, embed = embed)
            response = await client.wait_for_message(timeout=float(15), author=message.author, channel=message.channel)

            if response == None:
                await client.send_message(message.channel, '제대로 입력하지 않았습니다. 다시 시도해 주세요')
                return
            else:
                await client.delete_message(response)
                await client.delete_message(mudel)
                content = response.content.split(' ')
                hangul = re.compile('[ㄱ-ㅣ가-힣]+')
                if len(content) != 3 or hangul.findall(content[1]) != [] or hangul.findall(content[2]) != []:
                    await client.send_message(response.channel, '제대로 입력하지 않았습니다. 다시 시도해 주세요')

                else:
                    info_add(content, response.author.id)
        
        elif save_stat == 2:
            embed = discord.Embed(title='삭제하기', description='삭제할 정보의 사이트를 입력해 주세요')
            mudel = await client.send_message(message.channel, embed = embed)

        elif save_stat == 3:
            embed = discord.Embed(title='수정하기', description='수정할 id, 비밀번호와 그것의 사이트를 입력해 주세요')
            embed.add_field(name = '예시', value = '옥션 abcd1234 1234567')
            mudel = await client.send_message(message.channel, embed = embed)
    
    
    
    
    
    #심심이 관련 구문
    if message.content == 'sj 심심이' and message.channel.id == '577332815415476244':
        await client.send_message(message.channel, '심심이 작동 시작!')
        stat_chk[0] = 1
    
    if stat_chk[0] == 1 and message.channel.id == '577332815415476244' and message.content != '' and message.content != 'sj 심심이' and message.content != 'sj 종료' and message.contetn != 'sj 추가':
        embed, stat = find_res(message.content)
        if stat == -1:
            stat_chk[0] = 0
            mudel = await client.send_message(message.channel, embed = embed)
            response = await client.wait_for_message(timeout=float(15), author=message.author, channel=message.channel)
            if response == None:
                await client.send_message(message.channel, '시간이 초과되었습니다. 다시 시도해 주세요')
                return
            response.content.lower()
            if response.content == 'y':
                await client.send_message(message.channel, '[답변할말]을 적어주세요')
                response = await client.wait_for_message(timeout=float(15), author=message.author, channel=message.channel)

                if response == None:
                    await client.send_message(message.channel, '시간이 초과되었습니다. 다시 시도해 주세요')
                    return

                add_res_new(message.content, response.content)
                await client.send_message(response.channel, '추가 완료!')
                stat_chk[0] = 1
            elif response.content == 'n':
                await client.delete_message(response)
                await client.delete_message(mudel)
                stat_chk[0] = 1
                
        elif stat == 1:
            await client.send_message(message.channel, embed = embed)

    if message.content == 'sj 종료' and message.channel.id == '577332815415476244':
        stat_chk[0] = 0
        await client.send_message(message.channel, '심심이 종료!')

    if message.content == 'sj 추가' and message.channel.id == '577332815415476244' and stat_chk[0] == 0:
        await client.send_message(message.channel, '[들은말] [답변할말]을 띄어쓰기를 기준으로 적어주세요\n 예시) 안녕하세요 ㅎㅇ')
        response = await client.wait_for_message(timeout=float(15), author=message.author, channel=message.channel)
        if response == None:
            await client.send_message(message.channel, '시간이 초과되었습니다. 다시 시도해 주세요')
            return
        else:
            res = response.content.split(' ')
            add_res(res)
            await client.send_message(response.channel, '추가 완료!')

    if message.content == 'sj 삭제':
        await client.send_message(message.channel, '[들은말] [답변할말]을 띄어쓰기를 기준으로 적어주세요\n 예시) 안녕하세요 ㅎㅇ')
        response = await client.wait_for_message(timeout=float(15), author=message.author, channel=message.channel)
        if response == None:
            await client.send_message(message.channel, '시간이 초과되었습니다. 다시 시도해 주세요')
            return
        else:
            res = response.content.split(' ')
            stat = del_res(res)
            if stat == 1:
                await client.send_message(message.channel, '삭제 완료!')
            elif stat == -1:
                await client.send_message(message.channel, '삭제 실패(해당 답변 혹은 들은말이 존재하지 않음)')
            






client.run('NTY5NzY4NjgzMjMzMzQ1NTM3.XNjZJg.e8xjRhj1CmewVXTYCk9tPMGuW9U')