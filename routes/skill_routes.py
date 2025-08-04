from fastapi import APIRouter, Depends
from typing import List
from models.skill_model import Skill, SkillCategory
from models.user_model import User
from dependencies.auth import get_current_user
from services.skill_services import (
    add_category,
    add_skill_to_category,
    update_skill,
    delete_skill,
    get_all_skills
)

router = APIRouter()


@router.post("/skills/category")
async def create_category(category: SkillCategory, current_user: User = Depends(get_current_user)):
    return await add_category(category)

@router.post("/skills/{category_name}")
async def create_skill(category_name: str, skill: Skill, current_user: User = Depends(get_current_user)):
    return await add_skill_to_category(category_name, skill)

@router.put("/skills/{category_name}/{old_skill_name}")
async def modify_skill(category_name: str, old_skill_name: str, new_skill: Skill, current_user: User = Depends(get_current_user)):
    return await update_skill(category_name, old_skill_name, new_skill)

@router.delete("/skills/{category_name}/{skill_name}")
async def remove_skill(category_name: str, skill_name: str, current_user: User = Depends(get_current_user)):
    return await delete_skill(category_name, skill_name)

@router.get("/skills", response_model=List[SkillCategory])
async def fetch_all_skills(current_user: User = Depends(get_current_user)):
    return await get_all_skills()
