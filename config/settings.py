import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/yourdatabase")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
