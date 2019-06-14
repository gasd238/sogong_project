import asyncio
import discord
import re
from module.help import *
from module.check import *
from module.save import *
from module.simsim import *

client = discord.Client()
#심심이 플레이 상태 확인용 
stat_chk = 0

#sj save 명령어 사용 중 sj save 명령어 사용 안되도록
use_save = 0

#sj save 명령어 사용중 id pw 부분에 한글 입력 방지
hangul = re.compile('[ㄱ-ㅣ가-힣]+')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------------------')
    await client.change_presence(game=discord.Game(name="sj help로 도움말", type=0))

@client.event
async def on_message(message):
    #sj save 명령어 사용중 명령어를 쓸 수 없도록
    global use_save, stat_chk

    #혹시 봇이 명령어를 말했을때 무시하기 위한 코드
    if message.author.bot:
        return None

    #명령어 출력관련
    if message.content == 'sj help':
        await client.send_message(message.channel, embed = help())

    #개인정보 저장 관련 
    if message.content.startswith('sj save') and use_save == 0:
        CreateFileToBeSavedPrivacy()
        msg = message.content.split(' ')
        embed, save_stat = check_opt(msg)

        #use_save 를 1로 바꾸어 명령어 사용중 다른 명령어 사용 안되게 함
        use_save = 1

        #오류 처리(사용하지 않거나 잘못 입력 됬을시)
        if save_stat == 0 or save_stat == -1:
            await client.send_message(message.channel, embed = embed)
            use_save = 0

        #sj save 구문
        #-add 입력됬을시
        elif save_stat == 1:
            embed = discord.Embed(title='추가하기', description='저장할 id, 비밀번호와 그것의 사이트를 입력해 주세요')
            embed.add_field(name = '예시', value = '옥션 abcd1234 1234567')
            mudel = await client.send_message(message.channel, embed = embed)
            response = await client.wait_for_message(author=message.author, channel=message.channel)

            if response == None:
                await client.send_message(message.channel, '제대로 입력하지 않았습니다. 다시 시도해 주세요')
                use_save = 0
                return
            else:
                await client.delete_message(response)
                await client.delete_message(mudel)
                content = response.content.split(' ')

                if len(content) < 3 or len(content) > 4 or hangul.findall(content[1]) != [] or hangul.findall(content[2]) != []:
                    await client.send_message(response.channel, '제대로 입력하지 않았습니다. 다시 시도해 주세요')
                    use_save = 0

                elif len(content) == 3:
                    await client.send_message(message.channel, AddUserPrivacy(content[0], content[1], content[2], None, message.author.id))
                    use_save = 0

                else:
                    await client.send_message(message.channel, AddUserPrivacy(content[0], content[1], content[2], content[3], message.author.id))
                    use_save = 0
        
        #-del 이 입력됬을시
        elif save_stat == 2:
            embed = discord.Embed(title='삭제하기', description='삭제할 정보의 사이트를 입력해 주세요')
            mudel = await client.send_message(message.channel, embed = embed)
            response = await client.wait_for_message(author=message.author, channel=message.channel)

            if response == None:
                await client.send_message(message.channel, '제대로 입력하지 않았습니다. 다시 시도해 주세요')
                use_save = 0
                return
                
            else:
                await client.send_message(message.channel, DeleteUserPrivacy(response.content, message.author.id))
                await client.delete_message(response)
                await client.delete_message(mudel)           
                use_save = 0     

        #-mod가 입력됬을 시
        elif save_stat == 3:
            embed = discord.Embed(title='수정하기', description='수정할 id, 비밀번호와 그것의 사이트를 입력해 주세요')
            embed.add_field(name = '예시', value = '옥션 abcd1234 1234567')
            mudel = await client.send_message(message.channel, embed = embed)
            response = await client.wait_for_message(author=message.author, channel=message.channel)

            if response == None:
                await client.send_message(message.channel, '제대로 입력하지 않았습니다. 다시 시도해 주세요')
                use_save = 0
                return
            else:
                await client.delete_message(response)
                await client.delete_message(mudel)
                content = response.content.split(' ')
                if len(content) != 3 or hangul.findall(content[1]) != [] or hangul.findall(content[2]) != []:
                    await client.send_message(response.channel, '제대로 입력하지 않았습니다. 다시 시도해 주세요')
                    use_save = 0

                elif len(content) == 3:
                   await client.send_message(message.channel, AddUserPrivacy(content[0], content[1], content[2], None, message.author.id))
                   use_save = 0

                else:
                    await client.send_message(message.channel, AddUserPrivacy(content[0], content[1], content[2], content[3], message.author.id))
                    use_save = 0
             
        #-see가 입력됬을 시     
        elif save_stat == 4:
            embed = discord.Embed(title='정보 불러오기', description='불러올 정보의 사이트를 입력해 주세요')
            mudel = await client.send_message(message.channel, embed = embed)
            response = await client.wait_for_message(author=message.author, channel=message.channel)

            if response == None:
                await client.send_message(message.channel, '제대로 입력하지 않았습니다. 다시 시도해 주세요')
                use_save = 0
                return
                
            else:
                embed = discord.Embed(title='불러온 정보', description= response.content + '의 아이디 비밀 번호 에요!')
                embed.add_field(name = response.content, value = return_userInfoSelect(message.author.id, response.content))
                await client.send_message(message.channel, embed = embed)
                await client.delete_message(response)
                await client.delete_message(mudel)
                use_save = 0
    
    
    #심심이 관련 구문
    if message.content == 'sj 심심이' and message.channel.id == '577332815415476244':
        await client.send_message(message.channel, '심심이 작동 시작!')
        stat_chk = 1

    #정해진 심심이 방이 아닐 시
    elif message.content == 'sj 심심이' or message.content == 'sj 추가' and message.channel.id != '577332815415476244':
        await client.send_message(message.channel, '해당 채널에서는 심심이를 사용할 수 없습니다. 정해진 심심이 채널에서 사용해 주세요!')

    #stat_chk가 1이고 정해진 방에서만 작동시키는 명령어들 
    if stat_chk == 1 and message.channel.id == '577332815415476244' and message.content != '' and message.content != 'sj 심심이' and message.content != 'sj 종료' and message.content != 'sj 추가':
        embed, stat = find_res(message.content)

        #들은 말에 정해진 답변이 없을시 작동
        if stat == -1:
            stat_chk = 0
            mudel = await client.send_message(message.channel, embed = embed)
            response = await client.wait_for_message(timeout=float(15), author=message.author, channel=message.channel)
            if response == None:
                await client.send_message(message.channel, '시간이 초과되었습니다. 다시 시도해 주세요')
                return
            
            # y/n 입력시 Y/N 이 입력됬을때를 대비 소문자로 무조건 변경
            response.content.lower()

            #추가 하는 명령
            if response.content == 'y':
                await client.send_message(message.channel, '[답변할말]을 적어주세요')
                response = await client.wait_for_message(timeout=float(15), author=message.author, channel=message.channel)

                if response == None:
                    await client.send_message(message.channel, '시간이 초과되었습니다. 다시 시도해 주세요')
                    return

                # 답변 추가
                add_res_new(message.content, response.content)
                await client.send_message(response.channel, '추가 완료!')
                stat_chk = 1

            #추가 안함
            elif response.content == 'n':
                await client.delete_message(response)
                await client.delete_message(mudel)
                stat_chk = 1
        
        #답변이 있을 시 답변을 보냄
        elif stat == 1:
            await client.send_message(message.channel, embed = embed)


    #심심이 종료 구문
    if message.content == 'sj 종료' and message.channel.id == '577332815415476244':
        stat_chk = 0
        await client.send_message(message.channel, '심심이 종료!')

    #따로 들은말에 추가할 답변이 있을시 (심심이 작동중에는 작동하지 않음 코드가)
    if message.content == 'sj 추가' and message.channel.id == '577332815415476244' and stat_chk == 0:
        await client.send_message(message.channel, '[들은말] [답변할말]을 띄어쓰기를 기준으로 적어주세요\n 예시) 안녕하세요 ㅎㅇ')
        response = await client.wait_for_message(timeout=float(15), author=message.author, channel=message.channel)
        if response == None:
            await client.send_message(message.channel, '시간이 초과되었습니다. 다시 시도해 주세요')
            return
        else:
            res = response.content.split(' ')
            add_res(res)
            await client.send_message(response.channel, '추가 완료!')

    # 들은말에 답변 중 필요 없는것 삭제
    if message.content == 'sj 삭제' and stat_chk != 1:
        await client.send_message(message.channel, '[들은말] [삭제한말]을 띄어쓰기를 기준으로 적어주세요\n 예시) 안녕하세요 ㅎㅇ')
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


client.run('token')
