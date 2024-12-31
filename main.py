from fastapi import FastAPI

app=FastAPI(title="学习FastApi测试接口",deprecated="项目描述")


@app.get("/",summary="首页接口注释",description="首页接口描述",tags=["Index"])
def Index():
    return "Hello FastApi!"


