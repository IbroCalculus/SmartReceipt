from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Receipt(SQLModel, table=True):
    __tablename__ = "receipts"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    image_path: str
    merchant_name: Optional[str] = None
    total_amount: Optional[float] = None
    date_extracted: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    owner: Optional["User"] = Relationship(back_populates="receipts")
