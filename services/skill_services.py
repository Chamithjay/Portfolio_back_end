from database import get_skill_collection
from models.skill_model import  Skill, SkillCategory
from fastapi import HTTPException

async def add_category(category: SkillCategory):
    collection = get_skill_collection()
    existing = await collection.find_one({"name": category.name})
    if existing:
        raise HTTPException(status_code=400, detail="Category already exists")

    new_category = {
        "name": category.name,
        "skills": [skill.dict() for skill in category.skills]
    }

    await collection.insert_one(new_category)
    return {"message": "Category added successfully"}

async def add_skill_to_category(category_name: str, skill: Skill):
    collection = get_skill_collection()
    result = await collection.update_one(
        {"name": category_name},
        {"$push": {"skills": skill.dict()}},
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Skill added successfully"}

async def update_skill(category_name: str, old_skill_name: str, new_skill: Skill):
    collection = get_skill_collection()
    result = await collection.update_one(
        {"name": category_name, "skills.name": old_skill_name},
        {"$set": {"skills.$": new_skill.dict()}},
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Skill not found")
    return {"message": "Skill updated successfully"}

async def delete_skill(category_name: str, skill_name: str):
    collection = get_skill_collection()
    result = await collection.update_one(
        {"name": category_name},
        {"$pull": {"skills": {"name": skill_name}}},
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Skill not found or already removed")
    return {"message": "Skill removed successfully"}

async def get_all_skills():
    collection = get_skill_collection()
    categories = await collection.find().to_list(length=None)
    return categories
