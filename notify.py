import requests
import datetime
import os
import json

def send_wechat(title, content):
    """
    自包含的微信推送函数，直接从环境变量读取配置
    """
    # 直接在这里读取环境变量，不再依赖 config.py
    APP_ID = os.environ.get("WX_APP_ID", "")
    APP_SECRET = os.environ.get("WX_APP_SECRET", "")
    USER_ID = os.environ.get("WX_USER_ID", "")
    TEMPLATE_ID = os.environ.get("WX_TEMPLATE_ID", "")

    curr_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 检查配置
    if not all([APP_ID, APP_SECRET, USER_ID, TEMPLATE_ID]):
        print("❌ [微信配置缺失] 请检查青龙环境变量 WX_APP_ID, WX_APP_SECRET, WX_USER_ID, WX_TEMPLATE_ID")
        return False

    token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}"
    
    try:
        token_res = requests.get(token_url, timeout=10).json()
        access_token = token_res.get("access_token")
        
        if not access_token:
            print(f"❌ [Token获取失败] {token_res}")
            return False

        send_url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={access_token}"
        payload = {
            "touser": USER_ID,
            "template_id": TEMPLATE_ID,
            "data": {
                "item": {"value": title, "color": "#173177"},
                "time": {"value": curr_time, "color": "#173177"},
                "content": {"value": content, "color": "#333333"}
            }
        }

        response = requests.post(send_url, json=payload, timeout=10).json()
        
        if response.get("errcode") == 0:
            print(f"✅ [微信推送成功] {title}")
            return True
        else:
            print(f"❌ [微信推送失败] {response}")
            return False

    except Exception as e:
        print(f"❌ [微信推送异常] {str(e)}")
        return False
