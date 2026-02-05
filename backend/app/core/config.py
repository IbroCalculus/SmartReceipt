import os

class Settings:
    PROJECT_NAME: str = "SmartReceipt API"
    PROJECT_VERSION: str = "1.0.0"
    
    MYSQL_USER: str = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_ROOT_PASSWORD", "password")
    MYSQL_SERVER: str = os.getenv("MYSQL_SERVER", "db")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT", "3306")
    MYSQL_DB: str = os.getenv("MYSQL_DATABASE", "smartreceipt")
    
    # Using async driver 'aiomysql' for future proofing, or 'mysql-connector-python' for sync
    # For simplicity with SQLModel (which wraps SQLAlchemy), we typically use a sync driver for standard endpoints
    # Let's use standard 'mysql+mysqlconnector' to match requirements.txt choice
    DATABASE_URL: str = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"
    
    SECRET_KEY: str = os.getenv("JWT_SECRET", "supersecretkeyChangeThisInProduction")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
