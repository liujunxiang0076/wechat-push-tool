import os

# 从系统环境变量中读取，如果读取不到则默认为空字符串
# 这样即使你把这个文件推送到 GitHub，别人也看不到你的隐私数据
APP_ID = os.environ.get("WX_APP_ID", "")
APP_SECRET = os.environ.get("WX_APP_SECRET", "")
USER_ID = os.environ.get("WX_USER_ID", "")
TEMPLATE_ID = os.environ.get("WX_TEMPLATE_ID", "")

# 简单的校验逻辑，防止环境变量没配置导致程序报错
def check_config():
    missing = []
    if not APP_ID: missing.append("WX_APP_ID")
    if not APP_SECRET: missing.append("WX_APP_SECRET")
    if not USER_ID: missing.append("WX_USER_ID")
    if not TEMPLATE_ID: missing.append("WX_TEMPLATE_ID")
    
    if missing:
        print(f"❌ 配置缺失，请在青龙面板环境变量中添加: {', '.join(missing)}")
        return False
    return True
