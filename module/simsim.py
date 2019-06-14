import json
from random import randint
import discord

#json 파일 열기
def open_json():
    with open('Data/saved.json', 'r', encoding='utf-8') as resList:
        data = resList.read()
    data = json.loads(data)
    return data

#json 파일 저장
def save_json(data):
    with open('Data/saved.json', 'w', encoding='utf-8') as resList:
        json.dump(data, resList, ensure_ascii=False, indent="\t")

#json 새로운거 추가
def add_res_new(req, res):
    data = open_json()
    try:
        data['response'][req] = [str(res)]
    except:
        data["response"] = {}
        data['response'][req] = [str(res)]
    save_json(data)
    
#json 이미 있는 답변에 추가
def add_res(res):
    response = ''
    data = open_json()
    for i in range(1, len(res)):
        if i == len(res) - 1:
            response += res[i]
            break
        response +=res[i] +' '
    try:
        try:
            data['response'][res[0]].append(str(response))
        except:
            data['response'][res[0]] = [str(response)]
    except:
        data["response"] = {}
        try:
            data['response'][res[0]].append(str(response))
        except:
            data['response'][res[0]] = [str(response)]
    
    save_json(data)

#들은말에 답변 찾아 보내기
def find_res(req):
    data = open_json()
    try:
        num = randint(0, len(data['response'][str(req)])-1)
        embed = discord.Embed(title="답변", description=data['response'][str(req)][num])
        return embed, 1
    except:
        embed = discord.Embed(title="답변 없음", description="답변이 없습니다 추가하시겠습니까? y/n")
        return embed, -1

#들은말에 답변 찾아 삭제
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
        save_json(data)
        return 1
    except:
        return -1
    