from flask import Flask
from fszn import config

# 创建 Flask 应用
app = Flask(__name__, template_folder="templates", static_folder="static")
# 加载配置，例如从 config.py 的 Config 类
app.config.from_object('config.Config')

# 注册身份认证蓝图
from fszn.auth import auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')  # 将auth蓝图注册到应用:contentReference[oaicite:6]{index=6}

# （可选）注册其他蓝图，如主应用功能模块
# from fszn.main import main_bp
# app.register_blueprint(main_bp)

# 数据库初始化等操作...
