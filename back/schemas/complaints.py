from pydantic import BaseModel
from datetime import datetime
from .users import UserSchema

class ComplaintSchema(BaseModel):
    id: str
    user_id: str
    date: datetime
    at_moment: bool
    type: str
    neighborhood: str
    situation: str
    description: str
    created_at: datetime
    updated_at: datetime
    user: UserSchema | None

class ComplaintList(BaseModel):
    complaints: list[ComplaintSchema]


class ComplaintFilter(BaseModel):
    user_id: str
    from_date: datetime
    to_date: datetime
    query_string: str
    situation: str
    neighborhood: str
    type:str

class ComplaintUserSchema(BaseModel):
    id: str
    user_id: str
    date: datetime
    at_moment: bool
    type: str
    neighborhood: str
    situation: str
    description: str
    created_at: datetime
    updated_at: datetime
    user_name: str
    user_email: str
    user_phone_number: str
    user_birthdate: datetime
    user_gender: str
    user_ethnicity: str
    user_created_at: datetime
    user_updated_at: datetime

class ComplaintUserList(BaseModel):
    complaints: list[ComplaintUserSchema]


class CompalintListReturn(BaseModel):
    complaints: list[ComplaintUserSchema]
    max_pages:int
    size: int
