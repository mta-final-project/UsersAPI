from beanie import PydanticObjectId
from fastapi_users import schemas
from typing import Self
import re
from pydantic import model_validator


class UserRead(schemas.BaseUser[PydanticObjectId]):
    pass


class UserCreate(schemas.BaseUserCreate):
    @model_validator(mode="after")
    def check_domain(self) -> Self:
        match = re.search(r"@.+$", self.email)
        domain = match.group()
        if domain != "@mta.ac.il":
            raise ValueError("Invalid email domain. Only mta.ac.il is allowed.")
        return self


class UserUpdate(schemas.BaseUserUpdate):
    pass
