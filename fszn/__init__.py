from flask import Flask, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

# 全局 db 对象，供其它模块导入使用
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # 绑定 SQLAlchemy
    db.init_app(app)

    # 注册蓝图
    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # 主页路由：已登录显示欢迎，未登录跳登录页
    @app.route('/')
    def home():
        from .models import User
        user = None
        user_id = session.get('user_id')
        if user_id:
            user = User.query.get(user_id)
        return render_template('home.html', user=user)

    return app
