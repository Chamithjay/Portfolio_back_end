from pydantic import BaseModel
from typing import List, Optional

class Skill(BaseModel):
    name: str
    icon_base64: Optional[str] = None

class SkillCategory(BaseModel):
    name: str
    skills: List[Skill] = []