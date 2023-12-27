from fastapi import FastAPI
import uvicorn

app =FastAPI()

# GET method
@app.get("/")
async def get_root():
    return{"message:","GenShin activated!"}

# POST method 
# @app.post("/test/")
# async def creat_test():
#     pass

if __name__ =="__main__":
    uvicorn.run(app,host ="0.0.0.0")