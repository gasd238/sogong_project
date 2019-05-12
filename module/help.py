#명령어 설명 관련 모듈입니다.
import discord

def help():
    embed = discord.Embed(title="명령어",description='세종봇 명령어 모음', color=0xf7cac9)
    embed.add_field(name='sj 심심이', value="심심이 모드가 작동됨(다른 명령어 작동 불가(수정 예정))", inline=False)
    embed.add_field(name='sj save [-del, -add, -mod]', value="개인의 특정 사이트 아이디 비밀번호 저장기능 인수를 뒤에 꼭 붙여주어야 함\n-del은 삭제, -add는 추가, -mod는 수정", inline=False)
    return embed
