import base64
from database import get_profile_info_collection
from models.profile_model import ProfileBase
from typing import Optional, List
from fastapi import UploadFile, HTTPException

async def encode_file_to_base64(file: UploadFile) -> str:
    content = await file.read()
    return base64.b64encode(content).decode("utf-8")

async def save_profile(name, area_of_interest, github, linkedin, email, phone, photo, cv) -> ProfileBase:
    photo_base64 = await encode_file_to_base64(photo)
    cv_base64 = await encode_file_to_base64(cv)

    profile_doc = {
        "_id": "profile",  
        "name": name,
        "area_of_interest": area_of_interest,
        "github": github,
        "linkedin": linkedin,
        "email": email,
        "phone": phone,
        "photo_base64": photo_base64,
        "cv_base64": cv_base64,
    }

    collection = get_profile_info_collection()
    await collection.replace_one({"_id": "profile"}, profile_doc, upsert=True)

    return ProfileBase(**profile_doc)


async def update_profile(
    name: Optional[str] = None,
    area_of_interest: Optional[List[str]] = None,
    github: Optional[str] = None,
    linkedin: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
    photo: Optional[UploadFile] = None,
    cv: Optional[UploadFile] = None
) -> ProfileBase:
    update_fields = {}

    if name:
        update_fields["name"] = name
    if area_of_interest:
        update_fields["area_of_interest"] = area_of_interest
    if github:
        update_fields["github"] = github
    if linkedin:
        update_fields["linkedin"] = linkedin
    if email:
        update_fields["email"] = email
    if phone:
        update_fields["phone"] = phone
    if photo:
        update_fields["photo_base64"] = await encode_file_to_base64(photo)
    if cv:
        update_fields["cv_base64"] = await encode_file_to_base64(cv)

    if not update_fields:
        raise ValueError("No fields provided for update.")

    collection = get_profile_info_collection()
    await collection.update_one({}, {"$set": update_fields}, upsert=True)

    updated = await collection.find_one({})
    return ProfileBase(**updated)


async def get_profile() -> ProfileBase:
    collection = get_profile_info_collection()
    profile = await collection.find_one({"_id": "profile"})

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    profile.pop("_id", None)

    return ProfileBase(**profile)