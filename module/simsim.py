import json
from random import randint
import discord

def open_json():
    with open('Data/saved.json', 'r', encoding='utf-8') as resList:
        data = resList.read()
    data = json.loads(data)
    return data

def add_res_new(req, res):
    data = open_json()
    data['response'][req] = [str(res)]
    with open('Data/saved.json', 'w', encoding='utf-8') as resList:
        json.dump(data, resList, ensure_ascii=False, indent="\t")

def add_res(res):
    response = ''
    data = open_json()
    for i in range(1, len(res)):
        if i == len(res) - 1:
            response += res[i]
            break
        response +=res[i] +' '
    try:
        data['response'][res[0]].append(str(response))
    except:
        data['response'][res[0]] = [str(response)]
    with open('Data/saved.json', 'w', encoding='utf-8') as resList:
        json.dump(data, resList, ensure_ascii=False, indent="\t")

def find_res(req):
    data = open_json()
    try:
        num = randint(0, len(data['response'][str(req)])-1)
        embed = discord.Embed(title="답변", description=data['response'][str(req)][num])
        return embed, 1
    except:
        embed = discord.Embed(title="답변 없음", description="답변이 없습니다 추가하시겠습니까? y/n")
        return embed, -1

def del_res(re):
    response = ''
    for i in range(1, len(re)):
        if i == len(re) - 1:
            response += re[i]
            break
        response +=re[i] +' '
    data = open_json()
    try:
        data['response'][re[0]].remove(response)
        with open('Data/saved.json', 'w', encoding='utf-8') as resList:
            json.dump(data, resList, ensure_ascii=False, indent="\t")
        return 1
    except:
        return -1
    