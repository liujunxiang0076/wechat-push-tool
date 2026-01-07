import random
import datetime
from notify import send_wechat
from config import check_config

def get_fun_message():
    # 模拟一些有趣的消息池
    greetings = [
        "🌟 又是元气满满的一天！",
        "☕ 记得喝水，屏幕看久了歇一歇。",
        "🚀 服务器一切正常，正在为你保驾护航。",
        "🌙 熬夜辛苦了，早点休息哦。"
    ]
    
    # 模拟一点数据
    status_list = ["运行稳如老狗", "心情：极好", "状态：待机中", "CPU：正在摸鱼"]
    
    return random.choice(greetings), random.choice(status_list)

if __name__ == "__main__":
    if check_config():
        greet, status = get_fun_message()
        curr_time = datetime.datetime.now().strftime('%H:%M:%S')
        
        # 构造推送内容
        title = "📢 我的私人助手报到"
        content = f"{greet}\n当前时间：{curr_time}\n系统状态：{status}"
        
        print(f"正在推送自定义消息...")
        result = send_wechat(title, content)
        print(f"发送结果: {result}")
