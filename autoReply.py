import itchat, re, datetime, io, logging
from itchat.content import TEXT
from datetime import datetime

FORMAT = "[%(asctime)-15s] [%(levelname)-8s] %(message)s"

# 日志文件
handler = logging.FileHandler("msg.log", encoding="UTF-8")
handler.formatter = logging.Formatter(FORMAT)
logging.root.addHandler(handler)

handler = logging.StreamHandler()
handler.formatter = logging.Formatter(FORMAT)
logging.root.addHandler(handler)

logging.root.setLevel(logging.INFO)
logging.info('start')

# 只处理文本信息
@itchat.msg_register([TEXT])
def text_reply(msg):
    ''' 消息处理函数 '''
    # 正则匹配消息文本
    match = re.search('年|春', msg['Text'])
    # 排除自己发的内容和腾讯新闻发的内容
    if itchat.originInstance.storageClass.userName!=msg.FromUserName and msg.FromUserName != "newsapp" and match:
        # 自动回复
        msg.user.send('新春快乐！')
        # 记录日志
        log = f"{msg.user.NickName}"
        if msg.user.RemarkName:
            log += f"({msg.user.RemarkName})"
        log += f": {msg.Text}"
        # print(log, file=f, flush=True)
        # print(log)
        logging.info(log)

# 自动登陆
itchat.auto_login(hotReload=True)
itchat.run()
