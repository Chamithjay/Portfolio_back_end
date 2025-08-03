import base64
from database import get_profile_info_collection
from models.profile_model import ProfileBase
from typing import Optional, List
from fastapi import UploadFile

async def encode_file_to_base64(file: UploadFile) -> str:
    content = await file.read()
    return base64.b64encode(content).decode("utf-8")

# Create or replace full profile
async def save_profile(
    name: str,
    area_of_interest: List[str],
    github: Optional[str],
    linkedin: Optional[str],
    email: Optional[str],
    phone: Optional[str],
    photo: UploadFile,
    cv: UploadFile
) -> ProfileBase:
    photo_base64 = await encode_file_to_base64(photo)
    cv_base64 = await encode_file_to_base64(cv)

    profile_doc = {
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
    await collection.replace_one({}, profile_doc, upsert=True)

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
