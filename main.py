from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import close_mongo_connection, connect_to_mongo
from routes import auth_routes, profile_routes, skill_routes, project_routes

app = FastAPI()
origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()


@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

app.include_router(auth_routes.router, prefix="", tags=["auth"])
app.include_router(profile_routes.router, prefix="", tags=["profile"])
app.include_router(skill_routes.router, prefix="", tags=["skills"])
app.include_router(project_routes.router, prefix="", tags=["projects"])
