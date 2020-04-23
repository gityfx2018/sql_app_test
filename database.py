from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
SQLALCHEMY_DATABASE_URL ='mysql+pymysql://root:123456@127.0.0.1:3306/t_orm?charset=utf8'
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, max_overflow=5
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # sessionmaker 会话生成器

Base = declarative_base()
