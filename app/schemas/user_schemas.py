from pydantic import BaseModel, Field, field_validator


class UserCreate(BaseModel):
    username : str = Field(..., min_length=4)
    password : str = Field(..., min_length=4)
    repeat_password : str

    @field_validator("repeat_password")
    def passwords_match(cls, v, info):
        password = info.data.get("password")
        if password != v:
            raise ValueError("Passwords do not match")
        return v


class UserLogin(BaseModel):
    username : str
    password : str


class UserResponse(BaseModel):
    id : int
    token : str
