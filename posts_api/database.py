from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

DATABASE_URL= URL.create(
    "postgresql+psycopg",
    username="postgres.ibnsowjvyitjcvgoyvgw",
    password="Hnsa@2007Anu",
    host="aws-0-ap-northeast-1.pooler.supabase.com",
    port=6543,
    database="postgres",
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()