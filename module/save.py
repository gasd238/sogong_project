#-------------------------------------------------------------------------------------------
import getpass
import json
import os
from collections import OrderedDict
user = getpass.getuser()
fileDir = "C:/Users/" + user + "/AppData/Local/DiscordChatbot/UserPrivacy.json"
#폴더 만들기
def CreateDiscordChatbotFolder():
    folderDir = "C:/Users/" + user + "/AppData/Local/DiscordChatbot"
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

#CreateFileToBeSavedPrivacy()

#-------------------------------------------------------------------------------------------

#원하는 사이트의 아이디 비밀번호를 파일에서 불러오고 객체 리턴 
def ReadUserPrivacySelect(siteName):
    siteName = str(siteName)
    if os.path.isfile(fileDir):
        with open(fileDir, 'r', encoding='utf-8') as jsonFile:
            jsonData = json.load(jsonFile)
            if siteName in jsonData:
                return jsonData[siteName]
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
def AddUserPrivacy(siteName, ID, PW, etc):
    if etc == None:
        etc = "없음"
    siteName = str(siteName)
    ID = str(ID)
    PW = str(PW)
    etc = str(etc)
    if os.path.isfile(fileDir):
        userPrivacy = ReadUserPrivacySelectAll()
        userPrivacy[siteName] = {"id":ID, "PW":PW, "etc":etc}
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
def DeleteUserPrivacy(siteName):
    siteName = str(siteName)
    if os.path.isfile(fileDir):
        userPrivacy = ReadUserPrivacySelectAll()
        if siteName in userPrivacy:
            del userPrivacy[siteName]
            try:
                with open(fileDir, 'w', encoding='utf-8') as userinfo:
                    json.dump(userPrivacy, userinfo, ensure_ascii=False, indent="\t")
            except:
                return "삭제 실패"
            return "삭제 실패"
        else:
            return "삭제할 사이트가 발견되지 않음"
    else:
        return "삭제 실패"

#-------------------------------------------------------------------------------------------

#암호화 하여 리턴


#-------------------------------------------------------------------------------------------

#복호화 하여 리턴

#-------------------------------------------------------------------------------------------


