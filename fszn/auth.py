# 文件：fszn/auth.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form.get('email')
        # TODO: 验证输入...
        # 使用哈希后密码存储
        pwd_hash = generate_password_hash(password)  # 密码哈希加密:contentReference[oaicite:8]{index=8}
        # 将新用户插入数据库 (省略具体数据库操作)
        flash('注册成功，请登录')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 从数据库根据username获取用户记录 (省略查询代码)
        # 假设查询得到 user 对象，包含 user.password_hash
        # 验证密码哈希
        # if user and check_password_hash(user.password_hash, password):
        #     session['user_id'] = user.id  # 登录成功，在会话中记录用户
        #     return redirect(url_for('home'))
        # else:
        #     flash('用户名或密码不正确')
        pass
    return render_template('auth/login.html')
