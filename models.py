from pydantic import BaseModel, constr, EmailStr
from tortoise import Model
from tortoise import fields

class DateTimeModel(Model):
    create_at=fields.DatetimeField(auto_now_add=True,description="创建时间")
    update_at=fields.DatetimeField(auto_now=True,description="更新时间")

    class Meta:
        abstract=True

class User(DateTimeModel):
    id=fields.IntField(primary_key=True)
    username=fields.CharField(max_length=50,unique=True,description="用户名")
    email=fields.CharField(max_length=100,unique=True,description="邮箱")
    class Meta:
        table="user"


class UserCreate(BaseModel):
    username:constr(max_length=50)
    email:EmailStr

class UserResponse(BaseModel):
    id:int
    username:str
    email:str
    class Config:
        from_attributes=True