from tortoise import Model
from tortoise import fields

class DateTimeModel(Model):
    create_at=fields.DateField(auto_now_add=True,description="创建时间")
    update_at=fields.DateField(auto_now=True,description="更新时间")

    class Meta:
        abstract=True

class User(DateTimeModel):
    id=fields.IntField(primary_key=True)
    username=fields.CharField(max_length=50,unique=True,description="用户名")
    email=fields.CharField(max_length=100,unique=True,description="邮箱")
    class Meta:
        table="user"

