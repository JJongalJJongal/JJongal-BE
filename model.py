from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

#유저 성별
class Gender(str, Enum):
    male = "M"
    female = "F"

# 유저 역할
class Role(str, Enum): 
    admin = "admin"
    user = "user"
    student = "student"


class User(BaseModel):
    # Optional : 필수적으로 필요한 것은 아님
    id : Optional[UUID] = uuid4() # UUID : 범용 공유 식별자(Universally unique indentifier)
    first_name : str
    last_name : str
    middle_name : Optional[str]
    gender : Gender # class로 정의되어 있음
    roles : List[Role]
