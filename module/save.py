#-------------------------------------------------------------------------------------------
import getpass
import json
import os
from base64 import b64encode, b64decode
from collections import OrderedDict
from Cryptodome.Cipher import DES
user = getpass.getuser()
fileDir = "C:/Users/" + user + "/AppData/Local/DiscordChatbot/UserPrivacy.json"
folderDir = "C:/Users/" + user + "/AppData/Local/DiscordChatbot"
#폴더 만들기
def CreateDiscordChatbotFolder():
    if not os.path.isdir(folderDir):
        os.mkdir(folderDir)
    else:
        return False

#파일 만들기
def CreateUserPrivacyfile():
    from collections import OrderedDict
    file_data = OrderedDict()

    #file_data["GMARKET"]={"ID": "yoyowang0614", "PW":"gksruf0979", "data":"gksruf0979"}
    
    if not os.path.isfile(fileDir):
        with open(fileDir, 'w', encoding='utf-8') as make_file:
            json.dump(file_data, make_file, ensure_ascii=False, indent='\t')
    else:
        return False

#아이디 비밀번호가 저장될 파일 생성
def CreateFileToBeSavedPrivacy():
    CreateDiscordChatbotFolder()
    CreateUserPrivacyfile()


#-------------------------------------------------------------------------------------------

#원하는 사이트의 아이디 비밀번호를 파일에서 불러오고 객체 리턴 
def ReadUserPrivacySelect(uid, siteName):
    siteName = str(siteName)
    if os.path.isfile(fileDir):
        with open(fileDir, 'r', encoding='utf-8') as jsonFile:
            jsonData = json.load(jsonFile)
            if siteName in jsonData[uid]:
                return jsonData[uid][siteName]
            else:
                return False
    else:
        return False

#모든 사이트의 아이디 비밀번호를 파일에서 불러오고 객체 리턴
def ReadUserPrivacySelectAll():
    if os.path.isfile(fileDir):
        with open(fileDir, 'r', encoding='utf-8') as jsonFile:
            jsonData = json.load(jsonFile)
        return jsonData
    else:
        return False

# userPrivacy=ReadUserPrivacySelect('GMARKET')
# print(userPrivacy)

#-------------------------------------------------------------------------------------------

#아이디 비밀번호를 파일에 추가, 수정
def AddUserPrivacy(siteName, ID, PW, etc, uid):
    if etc == None:
        etc = "X"
    siteName = str(siteName)
    ID = str(ID)
    PW = str(PW)
    etc = str(etc)
    if os.path.isfile(fileDir):
        userPrivacy = ReadUserPrivacySelectAll()
        userPrivacy[uid][siteName]={"id":Encryption(uid[0:8], ID), "PW":Encryption(uid[0:8], PW), "etc":Encryption(uid[0:8], etc)}
        try:
            with open(fileDir, 'w', encoding='utf-8') as userinfo:
                json.dump(userPrivacy, userinfo, ensure_ascii=False, indent="\t")
        except:
            return "저장 실패"
        return "저장 성공"
    else:
        return "저장 실패"

# AddUserPrivacy("GG", "D", "B", "3")
# userPrivacy=ReadUserPrivacySelectAll()
# print(userPrivacy["GG"])

#-------------------------------------------------------------------------------------------

#아이디 비밀번호를 삭제
def DeleteUserPrivacy(siteName, uid):
    siteName = str(siteName)
    if os.path.isfile(fileDir):
        userPrivacy = ReadUserPrivacySelectAll()
        if siteName in userPrivacy:
            del userPrivacy[uid][siteName]
            try:
                with open(fileDir, 'w', encoding='utf-8') as userinfo:
                    json.dump(userPrivacy, userinfo, ensure_ascii=False, indent="\t")
            except:
                return "삭제 실패"
            return "삭제 성공"
        else:
            return "삭제할 사이트가 발견되지 않음"
    else:
        return "삭제 실패"

#-------------------------------------------------------------------------------------------

#문자열을 8바이트 배수 단위로 만드는 함수
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

#암호화 함수 - key는 무조건 8바이트(숫자혹은 문자8개)
#           - text는 한글 안됨
def Encryption(key, text):
<<<<<<< HEAD
    key = key.encode()
    des = DES.new(key, DES.MODE_ECB)

    padded_text = pad(text)
    encrypted_text = des.encrypt(padded_text.encode())
    return b64encode(encrypted_text).decode('utf-8')

#복호화 함수
def Decryption(key, encrypted_text):
    key = key.encode()
    des = DES.new(key, DES.MODE_ECB)

    decrypted_text = des.decrypt(encrypted_text)
    return decrypted_text.decode()

#-------------------------------------------------------------------------------------------\
def return_userInfoSelect(uid, siteName):
    userinfo = ReadUserPrivacySelect(uid, siteName)
    return_userinfo = "ID : " + Decryption(uid[0:8], b64decode(userinfo['id'])) + '\n' + "PW : " + Decryption(uid[0:8], b64decode(userinfo['PW'])) + '\n' + "etc : " + Decryption(uid[0:8], b64decode(userinfo['etc']))
    return return_userinfo
