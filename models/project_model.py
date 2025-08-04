from pydantic import BaseModel, HttpUrl
from typing import Optional

class Project(BaseModel):
    title: str
    description: Optional[str]
    image_base64: Optional[str]
    live_link: Optional[HttpUrl]
    github_link: Optional[HttpUrl]
