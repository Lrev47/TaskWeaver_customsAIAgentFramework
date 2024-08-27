from prisma import Prisma
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .settings import DATABASE_URL

# Initialize Prisma ORM
prisma = Prisma()

# SQLAlchemy setup (if you need direct SQLAlchemy integration as well)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Example of using Prisma
async def connect_prisma():
    await prisma.connect()

async def disconnect_prisma():
    await prisma.disconnect()
