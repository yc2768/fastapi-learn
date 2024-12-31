import logging
import uvicorn
from fastapi import FastAPI, HTTPException
from tortoise.contrib.fastapi import register_tortoise
from models import UserResponse, UserCreate, User

app=FastAPI(title="学习FastApi测试接口",deprecated="项目描述")


register_tortoise(
    app,
    db_url='mysql://root:root@localhost:3306/fastapilearn',  # 替换为你的 MySQL 用户名、密码和数据库名
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/",summary="首页接口注释",description="首页接口描述",tags=["index"])
async def index():
    return "Hello FastApi!"


@app.post("/user",response_model=UserResponse,summary="用户接口注释",description="新增用户",tags=["user"])
async def create_user(user:UserCreate):
    if await User.filter(username=user.username).exists():
        raise HTTPException(status_code=400, detail="用户已经存在!")
    user_info=await User.create(username=user.username,email=user.email)
    return user_info

@app.get("/user",response_model=list[UserResponse],summary="用户接口注释",description="获取所有用户",tags=["user"])
async def get_users():
    users= await User.all()
    return users

@app.get("/user/{user_id}",response_model=UserResponse,summary="用户接口注释",description="获取指定用户",tags=["user"])
async  def get_user(user_id:int):
    user=await User.get_or_none(id=user_id)
    if user is None:
        raise HTTPException(status_code=404,detail="用户不存在")
    return user

@app.put("/user/{user_id}",response_model=UserResponse,summary="用户接口注释",description="更新指定用户",tags=["user"])
async def update_user(user_id:int,user:UserCreate):
    user_obj=await User.get_or_none(id=user_id)
    if user_obj is None:
        raise HTTPException(status_code=404,detail="用户不存在")
    user_obj.username=user.username
    user_obj.email=user.email
    await user_obj.save()
    return user_obj

@app.delete("/user/{user_id}",response_model=dict,summary="用户接口注释",description="删除指定用户",tags=["user"])
async  def delete_user(user_id:int):
    user_obj = await User.get_or_none(id=user_id)
    if user_obj is None:
        raise HTTPException(status_code=404, detail="用户不存在")
    await user_obj.delete()
    return {"id":user_obj.id,"detail":"用户已删除"}



if __name__ == '__main__':

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, workers=1)


