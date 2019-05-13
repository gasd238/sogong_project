import json
from random import randint
import discord

def open_json():
    with open('Data/saved.json', 'r', encoding='utf-8') as userdata:
        data = userdata.read()
    data = json.loads(data)
    return data

def save_res():
    print(1)

def find_res(req):
    data = open_json()
    try:
        num = randint(0, len(data['response'][str(req)])-1)
        embed = discord.Embed(title="답변", description=data['response'][str(req)][num])
        return embed
    except:
        embed = discord.Embed(title="답변 없음", description="답변이 없습니다 추가하시겠습니까?")
        return embed