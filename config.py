# coding=utf-8
debug = False

SECRET_KEY = '9687d209a9ff0713da8edae47dce398fuckyoublog'

DB_FILE = 'blog.db'
DATABASE_URI =  'postgresql+psycopg2://gdgallhkmzucyp:BmSWLwkVV_Bfcjwz9sZPtSsIIX@ec2-54-243-50-213.compute-1.amazonaws.com:5432/d5sm1n1kpsj2ta'

ECHO = False

LOGGER_NAME = 'BLOG'

DEFAULT_ADMIN_LOGIN_NAME = 'admin'
DEFAULT_ADMIN_NICK_NAME = 'administrator'
DEFAULT_ADMIN_PASSWORD = '123456'
ADMIN_EMAIL = 'livoras@163.com'

TITLE = 'Livoras\' Blog'

POSTS_PER_PAGE = 7
TESTING = True

# email settings
SITE = 'http://livoras.com'
SENDER = 'noreplylivoras@163.com'
RECIEVER = 'me@livoras.com'
SMTP_SERVER = 'smtp.163.com'
SENDER_PASSWORD = 'crackmeplease.'
MAIL_CONTENT = u'''
<h1>Livoras</h1>
<h2>有个傻逼给你评论了你一下！</h2>
<div><a href="{link}">博客页面</a></div>
<div>TA的名字：{username}</div>
<div>TA的Email：{user_email}</div>
<div>TA说：{content}</div>
'''
