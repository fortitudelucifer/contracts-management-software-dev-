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

## 环境搭建
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
