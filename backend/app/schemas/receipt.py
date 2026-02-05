from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReceiptBase(BaseModel):
    merchant_name: Optional[str] = None
    total_amount: Optional[float] = None
    date_extracted: Optional[str] = None

class ReceiptCreate(ReceiptBase):
    pass

class Receipt(ReceiptBase):
    id: int
    user_id: int
    image_path: str
    created_at: datetime

    class Config:
        from_attributes = True
