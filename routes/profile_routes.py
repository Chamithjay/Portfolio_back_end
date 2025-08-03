from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import List, Optional
from services.profile_services import save_profile, update_profile, get_profile
from models.profile_model import ProfileBase

router = APIRouter()


@router.post("/profile", response_model=ProfileBase)
async def create_or_update_profile(
    name: str = Form(...),
    area_of_interest: List[str] = Form(...),
    github: Optional[str] = Form(None),
    linkedin: Optional[str] = Form(None),
    email: Optional[str] = Form(None),
    phone: Optional[str] = Form(None),
    photo: UploadFile = File(...),
    cv: UploadFile = File(...),
):
    try:
        profile = await save_profile(name, area_of_interest, github, linkedin, email, phone, photo, cv)
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/profile", response_model=ProfileBase)
async def partially_update_profile(
    name: Optional[str] = Form(None),
    area_of_interest: Optional[List[str]] = Form(None),
    github: Optional[str] = Form(None),
    linkedin: Optional[str] = Form(None),
    email: Optional[str] = Form(None),
    phone: Optional[str] = Form(None),
    photo: Optional[UploadFile] = File(None),
    cv: Optional[UploadFile] = File(None),
):
    try:
        profile = await update_profile(name, area_of_interest, github, linkedin, email, phone, photo, cv)
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/profile", response_model=ProfileBase)
async def read_profile():
    try:
        return await get_profile()
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))