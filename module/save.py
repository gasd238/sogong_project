#-------------------------------------------------------------------------------------------

#폴더 만들기
def CreateDiscordChatbotFolder():
    import os
    folderDir = "C:/Users/user/AppData/Local/DiscordChatbot"
    if not os.path.isdir(folderDir):
        os.mkdir(folderDir)
    else:
        return False

#파일 만들기
def CreateUserPrivacyfile():
    import os
    import json
    from collections import OrderedDict
    file_data = OrderedDict()

    #file_data["GMARKET"]={"ID": "yoyowang0614", "PW":"gksruf0979", "data":"gksruf0979"}

    fileDir = "C:/Users/user/AppData/Local/DiscordChatbot/UserPrivacy.json"
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
        import json
        import os
        fileDir = "C:/Users/user/AppData/Local/DiscordChatbot/UserPrivacy.json"
        siteName = str(siteName)
        if os.path.isfile(fileDir):
                with open(fileDir) as jsonFile:
                        jsonData = json.load(jsonFile)
                        if siteName in jsonData:
                                jsonString = jsonData[siteName]
                                return jsonString
                        else:
                                return False
        else:
                return False

#모든 사이트의 아이디 비밀번호를 파일에서 불러오고 객체 리턴
def ReadUserPrivacySelectAll():
        import json
        import os
        fileDir = "C:/Users/user/AppData/Local/DiscordChatbot/UserPrivacy.json"
        if os.path.isfile(fileDir):
                with open(fileDir) as jsonFile:
                        jsonData = json.load(jsonFile)
                        return jsonData
        else:
                return False

# userPrivacy=ReadUserPrivacySelect('GMARKET')
# print(userPrivacy)

#-------------------------------------------------------------------------------------------

#아이디 비밀번호를 파일에 추가, 수정
def AddUserPrivacy(siteName, ID, PW, etc):
        import os
        import json
        from collections import OrderedDict
        siteName = str(siteName)
        ID = str(ID)
        PW = str(PW)
        etc = str(etc)
        fileDir = "C:/Users/user/AppData/Local/DiscordChatbot/UserPrivacy.json"
        if os.path.isfile(fileDir):
                userPrivacy = ReadUserPrivacySelectAll()
                userPrivacy[siteName] = {"id":ID, "PW":PW, "etc":etc}
                jstring = json.dumps(userPrivacy, indent='\t')
                f = open(fileDir, "w", encoding='utf-8')
                f.write(jstring)
                f.close()
        else:
                return False

# AddUserPrivacy("GG", "D", "B", "3")
# userPrivacy=ReadUserPrivacySelectAll()
# print(userPrivacy["GG"])

#-------------------------------------------------------------------------------------------

#아이디 비밀번호를 삭제
def DeleteUserPrivacy(siteName):
        import os
        import json
        from collections import OrderedDict
        siteName = str(siteName)
        fileDir = "C:/Users/user/AppData/Local/DiscordChatbot/UserPrivacy.json"
        if os.path.isfile(fileDir):
                userPrivacy = ReadUserPrivacySelectAll()
                if siteName in userPrivacy:
                        del userPrivacy[siteName]
                        jstring = json.dumps(userPrivacy, indent='\t')
                        f = open(fileDir, "w", encoding='utf-8')
                        f.write(jstring)
                        f.close()
                else:
                        return False
        else:
                return False

#-------------------------------------------------------------------------------------------

#암호화 하여 리턴


#-------------------------------------------------------------------------------------------

#복호화 하여 리턴

#-------------------------------------------------------------------------------------------


