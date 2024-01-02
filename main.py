from fastapi import FastAPI
import uvicorn
from typing import Optional

app =FastAPI()

# dummy data
user = {"name":"David","email":"david@gmail.com"}

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
def put_user(name:str,email:str):
    user["name"]=name
    user["email"]=email
    return user

# PATCH method:
@app.patch("/api/user/{user_id}/")
def patch_user(user_id: int, name: Optional[str] = None, email: Optional[str] = None):
    if name:
        user["name"]=name
    if email:
        user["email"]=email
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
    