import uvicorn
from fastapi import FastAPI
from tortoise import Tortoise

app=FastAPI(title="学习FastApi测试接口",deprecated="项目描述")


async def initDb():
    await Tortoise.init(
                        db_url="mysql://root:root@localhost:3306/fastapilearn",
                        modules={"models":["models"]}
                      )
    await  Tortoise.generate_schemas()

@app.get("/",summary="首页接口注释",description="首页接口描述",tags=["Index"])
async def Index():
    # await initDb()
    return "Hello FastApi!"

if __name__ == '__main__':

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, workers=1)


