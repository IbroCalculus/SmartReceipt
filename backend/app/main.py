from fastapi import FastAPI
from sqlmodel import SQLModel
from app.database import engine
from app.routers import auth, receipts
# Import models so SQLModel metadata knows about them
from app.models import user, receipt

# Create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI(title="SmartReceipt API", version="1.0.0")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth.router, tags=["Authentication"])
app.include_router(receipts.router, tags=["Receipts"])

@app.get("/")
def read_root():
    return {"message": "Welcome to SmartReceipt API 🚀"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
