from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel
from fastapi import HTTPException
import json



app =FastAPI()


# dummy data
user = {"user_id":123,"name":"David","email":"david@gmail.com"} 


# define pydantic models
class User(BaseModel):
    user_id:int
    name:str
    email:str|None =None
    
    
class PutUser(BaseModel):
    user_id:int
    name:Optional[str]=None
    email:Optional[str]=None


# GET method(root)
@app.get("/")
async def get_root():
    return{"message:","GenShin activated!"}


# GET method(get all user data)
@app.get("/api/user")
def get_user():
    return user


# POST method
@app.post("/api/user")
def post_user(user_data:User):
    # check if it conforms User pydantic validation
    return {"user_id": user_data.user_id, "name": user_data.name, "email": user_data.email}

# @app.post("/api/user")
# def post_user(user_id:User["user_id"], name:User["name"],email:User["email"]):
#     user["user_id"]=user_id
#     user["name"]=name
#     user["email"]=email
#     return user


# PUT method 
@app.put("/api/user/{user_id}")
def put_user(user_id: int,user_data: User):
    if user_id != user_data.user_id:
        raise HTTPException(status_code=400, detail="user id mismatch")
    
    if user_data.name:
        user["name"] = user_data.name
    else:
        return{"message:","name required"}
        
    if user_data.email:
        user["email"]= user_data.email
    else:
        return{"message:","email required"}
        
    print("user_data:",user_data)
    
    return user


# PATCH method:
@app.patch("/api/user/{user_id}/")
def patch_user(user_id: int, user_data:User):
    if user_id != user_data.user_id:
        raise HTTPException(status_code=400, detail="user id mismatch")
    if user_data.name:
        user["name"] = user_data.name
    
    if user_data.email:
        user["email"]= user_data.email
        
    print("user_data:",user_data)
    
    return user


# DELETE method
@app.delete("/api/user/{user_id}/")
def delete_user(user_id: int):
    if user_id != user["user_id"]:
        raise HTTPException(status_code=400, detail="user id mismatch")
    user.clear()
    return {"message:","user deleted!"}


if __name__ =="__main__":
    uvicorn.run(app,host ="0.0.0.0")
    