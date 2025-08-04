from database import get_project_collection
from models.project_model import Project
from fastapi import HTTPException

def serialize_project(project: Project) -> dict:
    data = project.model_dump()  
    if "github_link" in data and data["github_link"] is not None:
        data["github_link"] = str(data["github_link"])
    if "live_link" in data and data["live_link"] is not None:
        data["live_link"] = str(data["live_link"])
    return data

async def add_project(project: Project):
    collection = get_project_collection()
    serialized_data = serialize_project(project)
    await collection.insert_one(serialized_data)
    return {"message": "Project added successfully"}

async def update_project(title: str, updated: Project):
    collection = get_project_collection()
    serialized_data = serialize_project(updated)
    result = await collection.update_one(
        {"title": title},
        {"$set": serialized_data}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project updated successfully"}

async def delete_project(title: str):
    collection = get_project_collection()
    result = await collection.delete_one({"title": title})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted successfully"}

async def get_all_projects():
    collection = get_project_collection()
    return await collection.find().to_list(length=None)
