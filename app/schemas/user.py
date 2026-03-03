from pydantic import BaseModel

class UserCreate(BaseModel):
    """
    Схема для создания пользователя
    """
    username: str
    email: str
    password: str
