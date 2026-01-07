import requests
import datetime
from config import APP_ID, APP_SECRET, USER_ID, TEMPLATE_ID

def send_wechat(title, content):
    # 1. 获取 Token
    token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}"
    token = requests.get(token_url).json().get("access_token")
    
    if not token:
        return "获取Token失败"

    # 2. 发送请求
    url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={token}"
    data = {
        "touser": USER_ID,
        "template_id": TEMPLATE_ID,
        "data": {
            "item": {"value": title, "color": "#173177"},
            "time": {"value": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')},
            "content": {"value": content, "color": "#FF0000"}
        }
    }
    return requests.post(url, json=data).json()
