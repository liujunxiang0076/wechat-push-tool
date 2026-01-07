import requests
import datetime
import os
import json
from config import APP_ID, APP_SECRET, USER_ID, TEMPLATE_ID

def send_wechat(title, content):
    """
    增强版通用推送函数
    """
    curr_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 1. 获取 Access Token
    token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}"
    
    try:
        # 设置 10 秒超时，防止网络卡死
        token_res = requests.get(token_url, timeout=10).json()
        access_token = token_res.get("access_token")
        
        if not access_token:
            error_msg = f"❌ [Token获取失败] 错误码: {token_res.get('errcode')} 原因: {token_res.get('errmsg')}"
            print(error_msg)
            return False

        # 2. 构造推送数据
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

        # 3. 执行发送
        response = requests.post(send_url, json=payload, timeout=10).json()
        
        if response.get("errcode") == 0:
            print(f"✅ [推送成功] 标题: {title} | 时间: {curr_time}")
            return True
        else:
            # 记录详细的微信返回错误
            error_log = f"❌ [推送失败] 微信返回: {json.dumps(response, ensure_ascii=False)}"
            print(error_log)
            return False

    except requests.exceptions.Timeout:
        print(f"❌ [网络超时] 连接微信服务器超时，请检查 VPS 网络。")
    except Exception as e:
        print(f"❌ [程序异常] 发生了未预料的错误: {str(e)}")
    
    return False
