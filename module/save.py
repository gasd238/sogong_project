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

#문자열을 8바이트 배수 단위로 만드는 함수
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

#암호화 함수 - key는 무조건 8바이트(숫자혹은 문자8개)
#           - text는 한글 안됨
def Encryption(key, text):
        from Crypto.Cipher import DES

        key = key.encode()
        des = DES.new(key, DES.MODE_ECB)

        padded_text = pad(text)
        encrypted_text = des.encrypt(padded_text.encode())

        return encrypted_text

#복호화 함수
def Decryption(key, encrypted_text):
        from Crypto.Cipher import DES

        key = key.encode()
        des = DES.new(key, DES.MODE_ECB)

        decrypted_text = des.decrypt(encrypted_text).decode()

        return decrypted_text

key = 'abcdefg1'
text = 'yoyowang0614**@gmail.com'

print("원본: " + text)

encrypted_text = Encryption(key, text)

print("DES 암호화된 자료:")
print(encrypted_text)

decrypted_text = Decryption(key, encrypted_text)

print("복호: " + decrypted_text)