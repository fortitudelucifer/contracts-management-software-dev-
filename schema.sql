-- 1. 创建数据库
CREATE DATABASE FSZN_DB;
GO

-- 2. 创建登录账号
CREATE LOGIN fszn_user WITH PASSWORD = 'YourStrongPassword123!';
GO

-- 3. 在数据库中为这个登录创建用户，并赋予 db_owner 权限
USE FSZN_DB;
GO

CREATE USER fszn_user FOR LOGIN fszn_user;
GO

ALTER ROLE db_owner ADD MEMBER fszn_user;
GO
