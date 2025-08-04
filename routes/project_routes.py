from fastapi import APIRouter, Depends
from typing import List
from models.project_model import Project
from models.user_model import User
from dependencies.auth import get_current_user
from services.project_services import (
    add_project, update_project, delete_project, get_all_projects
)

router = APIRouter()

@router.post("/projects")
async def create_project(project: Project, current_user: User = Depends(get_current_user)):
    return await add_project(project)

@router.put("/projects/{title}")
async def modify_project(title: str, project: Project, current_user: User = Depends(get_current_user)):
    return await update_project(title, project)

@router.delete("/projects/{title}")
async def remove_project(title: str, current_user: User = Depends(get_current_user)):
    return await delete_project(title)

@router.get("/projects", response_model=List[Project])
async def fetch_projects(current_user: User = Depends(get_current_user)):
    return await get_all_projects()
