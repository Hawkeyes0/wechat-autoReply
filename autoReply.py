import itchat, re, datetime, io
from itchat.content import TEXT
from datetime import datetime

# 日志文件
f = open("msg.log", "a", encoding="utf-8")
print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}] start", file=f, flush=True)

# 只处理文本信息
@itchat.msg_register([TEXT])
def text_reply(msg):
    ''' 消息处理函数 '''
    # 正则匹配消息文本
    match = re.search('年|春', msg['Text'])
    # 获知发送人信息
    user = itchat.search_friends(userName=msg['FromUserName'])
    if match:
        # 自动回复
        itchat.send(('新春快乐！'), msg['FromUserName'])
        # 记录日志
        log = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}] {user['NickName']}"
        if user['RemarkName']:
            log += "(" + user['RemarkName'] + ")"
        log += ": " + msg['Text']
        print(log, file=f, flush=True)
        print(log)

# 自动登陆
itchat.auto_login(hotReload=True)
itchat.run()
f.close()
