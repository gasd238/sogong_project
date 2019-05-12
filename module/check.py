#인수등 모든 check 관련 기능을 모아둔 모듈
import discord

option_list = ['-del', '-add', '-mod']

def check_opt(msg):
    save_stat = 0
    if len(msg) == 3:
        for i in option_list:
            if msg[2] == i:
                embed = discord.Embed(title = i, description = i)
                if i == '-add':
                    save_stat = 1
                elif i == '-del':
                    save_stat = 2
                else:
                    save_stat = 3
                break
            else:
                embed = discord.Embed(title = 'Error', description = '잘못된 인수가 입력되었습니다.\n\nsj save -add[추가]\nsj save -del[삭제]\nsj save -mod[수정]')
        return embed, save_stat
    else:
        embed = discord.Embed(title = 'Error', description = '인수가 입력되지 않았습니다.\n\nsj save -add[추가]\nsj save -del[삭제]\nsj save -mod[수정]')
        return embed, -1