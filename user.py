from fastapi import APIRouter, HTTPException
from pydantic import BaseModel 
from typing import Union, List
import uuid
from jose import jwt

from cred import saveUsersDB, getUsersDB

SECRET_KEY = "Tester"

#the secret key is used to create the annonymity for the users credentials.

router = APIRouter()

class UserCredentials(BaseModel):
    email: str
    password: str
    display_name: str = None

class UserData(BaseModel):
    email: str
    password: str
    display_name: str = None

class LoginResponse(BaseModel):
    access_token : str
    user: UserData

#the classes consist of different credentials, this is so that they can target different functions of the login and register system. 
#the usercredentials consists of the users information that is required for register, the userdata holds the information for the user to login after being registered. 
#the loginresponse creates the annonymity using the access token and uses the userdata to allow the user to login to the website. 

@router.post("/register", response_model=LoginResponse)
async def register_user(credentials: UserCredentials):
    users = getUsersDB()
    if credentials.email in users:
        raise HTTPException(400, detail="account already exists")

    new_user = {
        "id" : str(uuid.uuid4()),
        "email": credentials.email,
        "password": credentials.password,
        "display_name": credentials.display_name
    }

    new_token = {
        "sub": new_user["id"]
    }

    token = jwt.encode(new_token, SECRET_KEY, algorithm="HS256")

    new_user["access_token"] = token

    users[credentials.email] = new_user

    saveUsersDB(new_user)
    
    return {"access_token" : token, "user" : users[credentials.email]}

#the register module consists of creating a new user, what credentials will be required from the user. 
#the token function creates the annonymity for the user to be able to access their account once they are registered. 
#the new user and user function saves the credentials to the users registered account. 

@router.post("/login", response_model=LoginResponse)
async def login_user(user: UserCredentials):
    users = getUsersDB()
    if not user.email in users:
        raise HTTPException(400, detail="account doesent exist")
    if not user.password == users[user.email]["password"]:
        raise HTTPException(400, detail="account already exists")



    new_token = {
        "sub": users[user.email]["id"]
    }


    token = jwt.encode(new_token, SECRET_KEY, algorithm="HS256")

    user[user.email]["access_token"] = token

    saveUsersDB(user)

    return {"access_token" : token, "user" : users[user.email]}

#the login module contains the information for the users to login. 
#the email and password function is implemented to let the user know whether their account exists or not. 
#the return function for both the register and login function allows the accounts to be creted after the whole process. 