from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlmodel import Session, select
from typing import List
import shutil
import os
import uuid

from app import database
from app.models import receipt as models
from app.models import user as user_models
from app.routers import auth
# from app.schemas import receipt as schemas # Not using separate schemas for now with SQLModel

router = APIRouter()

# TODO: Refactor Auth into shared dependency
from jose import JWTError, jwt
from app.core.config import settings

async def get_current_active_user(token: str = Depends(auth.oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    statement = select(user_models.User).where(user_models.User.email == email)
    results = db.exec(statement)
    user = results.first()
    
    if user is None:
        raise credentials_exception
    return user


@router.post("/receipts/", response_model=models.Receipt)
async def upload_receipt(
    file: UploadFile = File(...), 
    current_user: user_models.User = Depends(get_current_active_user),
    db: Session = Depends(database.get_db)
):
    # 1. Save File
    file_id = str(uuid.uuid4())
    ext = file.filename.split('.')[-1]
    file_path = f"uploads/{file_id}.{ext}"
    
    os.makedirs("uploads", exist_ok=True)
    
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
        
    # 2. Perform OCR (Mock for now or real if tesseract installed)
    from app.services import ocr
    try:
        extracted_data = await ocr.extract_text_from_image(content)
    except Exception:
         # Fallback if OCR fails or mock
         extracted_data = {
             "merchant_name": "Unknown Merchant",
             "total_amount": 0.0,
             "date_extracted": None
         }
    
    # 3. Save to DB
    db_receipt = models.Receipt(
        user_id=current_user.id,
        image_path=file_path,
        merchant_name=extracted_data.get("merchant_name"),
        total_amount=extracted_data.get("total_amount"),
        date_extracted=extracted_data.get("date_extracted")
    )
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)
    
    return db_receipt

@router.get("/receipts/", response_model=List[models.Receipt])
def read_receipts(
    skip: int = 0, 
    limit: int = 100, 
    current_user: user_models.User = Depends(get_current_active_user),
    db: Session = Depends(database.get_db)
):
    statement = select(models.Receipt).where(models.Receipt.user_id == current_user.id).offset(skip).limit(limit)
    receipts = db.exec(statement).all()
    return receipts
