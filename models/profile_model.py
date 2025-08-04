from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional, List

class ProfileBase(BaseModel):
    name: str
    area_of_interest: List[str]
    github: Optional[HttpUrl]
    linkedin: Optional[HttpUrl]
    email: Optional[EmailStr]
    phone: Optional[str]
    photo_base64: Optional[str]  
    cv_base64: Optional[str]     