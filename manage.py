# -*- coding: utf-8 -*-
# @Author  : junjunzai
# @Email   : junjunzai@163.com
# @File    : manage.py
# @Software: PyCharm

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_session import Session

app = Flask(__name__)




class Config(object):
    """工程配置信息"""

    DEBUG = True

    #配置数据库信息
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/information"
    #设置数据库跟踪
    SQLALCHEMY_TRACK_MODIFICATIONS = Flask

    #配置redis信息
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    #flask_session的配置信息
    #指定session保存到redis中
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True #让cookie中的session_id被加密处理
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT) #使用redis实例
    PERMANENT_SESSION_LIFETIME = 86400



app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
CSRFProtect(app)
Session(app)


@app.route('/')
def index():
    return 'index page88888'

if __name__ == '__main__':
    app.run(debug=True)


