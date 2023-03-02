import os

from flask import Flask, request
from wechatpy import parse_message
from wechatpy.replies import TextReply

app = Flask(__name__)

# 主页
@app.route('/')
def hello_world():
    return '欢迎来到HsuHeinrich的世界'


# 消息推送
@app.route('/message/post', methods=['GET', 'POST'])
def wechat_message():
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')
    
    if request.method == 'GET':
        # 验证服务器
        return echostr
    
    if request.method == 'POST':
        # 处理公众号消息
        xml = request.stream.read().decode('utf-8')
        msg = parse_message(xml)
        
        if msg.type == 'text':
            reply = TextReply(content=msg.content, message=msg)
            return reply.render()


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 80)))