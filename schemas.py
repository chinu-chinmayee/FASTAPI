from pydantic import BaseModel,EmailStr,Field
from typing import Optional
from datetime import datetime
    
class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True

class PostCreate(PostBase):
    pass
        
class post(PostBase):
    id:int
    created_at:datetime

    class Config:
        orm_mode=True

class UserCreate(BaseModel):
    email:EmailStr
    password:str=Field(...,max_length=72)

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime

    class Config:
        orm_mode=True
        


    
    


