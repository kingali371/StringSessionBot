import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# استخدم SQLite محلياً
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///database.db")

# إذا كان الرابط MongoDB حوله إلى SQLite
if DATABASE_URL and DATABASE_URL.startswith("mongodb"):
    print("⚠️ MongoDB غير مدعوم، استخدام SQLite بدلاً من ذلك")
    DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SESSION = scoped_session(sessionmaker(bind=engine))

def start():
    return SESSION

# إنشاء الجداول إذا لم تكن موجودة
from StringSessionBot.database.users import Users
from StringSessionBot.database.blacklist import BlackList
from StringSessionBot.database.banned import Banned

Users.__table__.create(engine, checkfirst=True)
BlackList.__table__.create(engine, checkfirst=True)
Banned.__table__.create(engine, checkfirst=True)
