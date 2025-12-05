# contracts-management-software-dev
contracts management software dev  process
reference: https://www.bilibili.com/video/BV13o4y1V7Jb?spm_id_from=333.788.videopod.episodes&vd_source=d49e0c134bc6c6180dab2a3de3c221f0

## Sql Server 2022 developer
安装windows11版和ubuntu 24.04版
### windows11
安装时 SQL Server Browser 选项选为自动
SQLServer 2022 配置管理器-网络配置-把TCP/IP启用
#### 防火墙设置
- 设置
- 隐私与安全性
- windows安全中心
- 防火墙和网络保护
- 允许应用通过防火墙
- 更改设置
- 允许其他应用
- 打开 C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Binn\sqlservr.exe
- 添加
- 打开 C:\Program Files\Microsoft SQL Server\90\Shared\sqlwriter.exe
- 添加
- 打开 C:\Program Files (x86)\Microsoft SQL Server\90\Shared\sqlbrowser.exe
- 添加
- 确定

#### employ sql server
- 新建查询
   - create detabase [name]
- 最好用一个test用户来测试数据库
- select
   - order
   - desc
- delete
- update
- join
- drop
- 注释 --

### ubuntu24.04
```bash
curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
```
```bash
curl -fsSL https://packages.microsoft.com/config/ubuntu/24.04/mssql-server-preview.list | sudo tee /etc/apt/sources.list.d/mssql-server-preview.list
```
```bash
sudo apt-get update
sudo apt-get install -y mssql-server
```
- 设置密码
```bash
sudo /opt/mssql/bin/mssql-conf setup
```
- 查看运行状态
```
systemctl status mssql-server --no-pager
```
未完待续 tbc



## Sql Server management studio 2022
尽量都安装全，方便全流程的开发

# 项目框架
```text
fszn_contract/
├── fszn/                   # 应用包
│   ├── __init__.py
│   ├── models.py
│   ├── auth.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── auth/
│   │       ├── login.html
│   │       └── register.html
│   └── static/             # 先空着，以后放 CSS/JS
├── config.py
├── requirements.txt        # 已有
└── run.py
```
## 环境搭建
1.本机创建项目和虚拟环境
```cmd
D:\code> mkdir fszn_contract
D:\code> cd fszn_contract
D:\code\fszn_contract> py -3 -m venv venv
D:\code\fszn_contract> venv\Scripts\activate
```
```
# requirement.txt
Flask
Flask-SQLAlchemy
pyodbc
python-dotenv
```
```cmd
(venv) D:\code\fszn_contract> pip install -r requirements.txt
```
2.在SQL Server里创建数据库和专用账号（有 SQL Server 2022 Developer + SSMS 22）
1.打开SMSS 22，连接测试用的实例
2.
```sql
-- 1. 创建数据库
CREATE DATABASE FSZN_DB;
GO

-- 2. 创建登录账号（注意把密码改成你自己的强密码）
CREATE LOGIN fszn_user WITH PASSWORD = 'YourStrongPassword123!';
GO

-- 3. 在数据库中为这个登录创建用户，并赋予 db_owner 权限
USE FSZN_DB;
GO

CREATE USER fszn_user FOR LOGIN fszn_user;
GO

ALTER ROLE db_owner ADD MEMBER fszn_user;
GO
```
3.在SMSS 22里确认有
- 数据库 FSZN_DB
- 安全性→登录名fsnz_user
- FSZN_DB→安全性→用户里有fsnz_user

4.写配置文件config.py

5.flask应用初始化fszn/init.py

6.定义用户模型fszn/models.py

7.身份认证蓝图fszn/auth.py（注册 + 登录 + 退出）

8.基础模板fszn/templates/base.html

9.主页模板fszn/templates/home.html

10.登录/注册模板fszn/templates/auth/login.html和fszn/templates/auth/register.html

11.启动入口run.py

12.运行与测试
  - 确认虚拟环境已激活（命令行前有 (venv)）
  - 在项目根目录执行: (venv) D:\code\fszn_contract> python run.py
  - 浏览器打开：http://127.0.0.1:5000/
 
### 遇到的问题
#### 虚拟环境venv打不开
解决方法：用管理员权限打开cmd，然后cd改变路径直到目标路径

#### Non-UTF-8中文报错，visual studio默认用了CRLF编码
解决方法，在vscode和visual studio里都将编码默认模式确定为“无签名的UTF-8”，且将所有html文件重写了一遍

#### 以一种访问权限不允许的方式做了一个访问套接字的尝试。
修改 run.py，换一个端口 + 明确 host

#### git设置ssh公钥
解决方法：
```git bash
ssh-keygen -t ed25519 -C "你的邮箱"
```
三次回车

##### 每次新建仓库都要 git remote set-url origin git@github.com:fortitudelucifer/neme of repositories.git

#### 在终端输入netstat -ano | findstr :5000 netstat -ano | findstr :5001后没有任何反馈
解决方法：用一个最小 socket 测试确认是系统拦截

#### 增删新条目的时候sql的条目自增
解决方法：设置一个display_order
