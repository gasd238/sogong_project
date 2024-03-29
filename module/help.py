#명령어 설명 관련 모듈입니다.
import discord

def help():
    embed = discord.Embed(title="명령어",description='세종봇 명령어 모음', color=0xf7cac9)
    embed.add_field(name='sj 심심이', value="심심이 모드가 작동됩니다.(심심이 채팅방에서만 사용 가능)", inline=False)
    embed.add_field(name='sj 종료', value="심심이 모드가 종료됩니다.(심심이 채팅방에서만 사용 가능)", inline=False)
    embed.add_field(name='sj 종료', value="심심이 답변을 추가합니다.(심심이 모드가 종료상태일때만 사용가능, 심심이 채팅방에서만 사용 가능)", inline=False)
    embed.add_field(name='sj save [-del, -add, -mod, -see]', value="개인의 특정 사이트 아이디 비밀번호 저장기능 인수를 뒤에 꼭 붙여주어야 함\n-del은 삭제, -add는 추가, -mod는 수정, -see는 보기", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/avatars/427797391953887232/4aa545afad35506a44bfb1ea3a76fe0a.webp?size=1024")
    return embed
