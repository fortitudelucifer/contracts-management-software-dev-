class Config:
    SECRET_KEY = 'dev-secret-key'  # 会话秘钥，用于安全目的（请在生产环境中修改）
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/fszn_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
