from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    password_confirm: str
    age: int
    email: int


class User(BaseModel):
    id: int
    username: str
    age: int

    class Config:
        orm_mode = True


class Pet(BaseModel):
    id: int
    name: str
    age: int
    species: str
    breed: str

    class Config:
        orm_mode = True