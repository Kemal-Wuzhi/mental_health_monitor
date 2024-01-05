from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel

app =FastAPI()

# dummy data
user = {"name":"David","email":"david@gmail.com"} 

# define pydantic models
class User(BaseModel):
    name:str
    email:str
    
class PutUser(BaseModel):
    name:Optional[str]=None
    email:Optional[str]=None

# GET method
@app.get("/")
async def get_root():
    return{"message:","GenShin activated!"}

# POST method
@app.post("/api/user")
def post_user(user_id: int,name:str,email:str):
    user["name"]=name
    user["email"]=email
    return user

# PUT method 
@app.put("/api/user/{user_id}")
def put_user(name:str,user_data:str):
    user["name"]=user_data.name
    user["email"]=user_data.email
    return user

# PATCH method:
@app.patch("/api/user/{user_id}/")
def patch_user(user_id: int, user_data=PutUser):
    if user_data.name:
        user["name"]=user_data.name
    if user_data.email:
        user["email"]=user_data.email
    return user    


# DELETE method
@app.delete("/api/user/{user_id}/")
def delete_test(user_id: int):
    if user_id !=1:
        # TODO:exception
        pass
    user.clear()
    return {"message:","user deleted!"}


if __name__ =="__main__":
    uvicorn.run(app,host ="0.0.0.0")
    