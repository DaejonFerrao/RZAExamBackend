from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

import user

app = FastAPI()

origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:3000",
    "https://localhost:3000"
]

#the origins functionality is to ensure that the website and the fastapi application can connect together. 

app.add_middleware(
    CORSMiddleware,
    allow_credentials = True,
    allow_origins = origins,
    allow_headers =["*"],
    allow_methods =["*"],
)

#the middleware applications control the visual and functionality of the fastapi application. 

app.include_router(user.router, prefix="/users", tags=["users"])

#the app include allows the user module to be seen on the fastapi application, This is also used for testing the website. 

@app.get("/")
async def root():
    return {"message" : "Welcome to FastAPI"}

#this function is just to show that the application is running and the message displays welcome to fastapi
