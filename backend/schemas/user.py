from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
import uuid


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None


class UserResponse(UserBase):
    user_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class User(UserBase):
    user_id: str = Field(default_factory=lambda: str(uuid.uuid4()))

    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None

    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
