import itchat, re, logging
from itchat.content import TEXT

FORMAT = "[%(asctime)-15s] [%(levelname)-8s] file \"%(pathname)s\", line %(lineno)d, in %(funcName)s \n\t%(message)s"

# 日志文件
handler = logging.FileHandler("msg.log", encoding="UTF-8")
handler.formatter = logging.Formatter(FORMAT)
logging.root.addHandler(handler)

handler = logging.StreamHandler()
handler.formatter = logging.Formatter(FORMAT)
logging.root.addHandler(handler)

logger = logging.getLogger('autoReply')
logger.setLevel(logging.INFO)
logger.info('start')

# 只处理文本信息
@itchat.msg_register([TEXT])
def text_reply(msg):
    ''' 消息处理函数 '''
    # 正则匹配消息文本
    match = re.search('年|春', msg['Text'])
    # 排除自己发的内容和腾讯新闻发的内容
    if itchat.originInstance.storageClass.userName!=msg.FromUserName and msg.FromUserName != "newsapp" and match:
        # 自动回复
        msg.user.send('新春快乐！年年有鱼！')
        # 记录日志
        log = f"{msg.user.NickName}"
        if msg.user.RemarkName:
            log += f"({msg.user.RemarkName})"
        log += f": \n{msg.Text}"
        # print(log, file=f, flush=True)
        # print(log)
        logger.info(log)

group_send = []
@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
    ''' 群消息处理 '''
    # 正则匹配消息文本
    match = re.search('年|春', msg['Text'])
    # 排除自己发的内容和已经回复的群
    if msg.isAt:
        msg.user.send(u'@%s\u2005新春快乐！年年有鱼！' % (msg.ActualNickName))
        log = u'[%s] %s: \n%s' % (msg.user.NickName, msg.ActualNickName, msg.Text)
        logger.info(log)
    elif itchat.originInstance.storageClass.userName!=msg.ActualUserName and msg.FromUserName not in group_send and match:
        msg.user.send('新春快乐！年年有鱼！')
        group_send.append(msg.FromUserName)
        log = u'[%s] %s: \n%s' % (msg.user.NickName, msg.ActualNickName, msg.Text)
        logger.info(log)

# 自动登陆
itchat.auto_login(hotReload=True)
itchat.run()
