from notify import send_wechat

if __name__ == "__main__":
    print("开始测试微信推送...")
    result = send_wechat("项目更新提醒", "测试项目 wechat-push-tool 已成功在青龙面板运行！")
    print(f"发送结果: {result}")
