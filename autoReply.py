import itchat, re, datetime, io
from itchat.content import TEXT
from datetime import datetime

f = open("msg.log", "a", encoding="utf-8")
print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}] start", file=f, flush=True)

@itchat.msg_register([TEXT])
def text_reply(msg):
    match = re.search('年|春', msg['Text'])
    user = itchat.search_friends(userName=msg['FromUserName'])
    if match:
        itchat.send(('新春快乐！'), msg['FromUserName'])
        log = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}] {user['NickName']}"
        if user['RemarkName']:
            log += "(" + user['RemarkName'] + ")"
        log += ": " + msg['Text']
        print(log, file=f, flush=True)
        print(log)

itchat.auto_login(hotReload=True)
itchat.run()
f.close()
