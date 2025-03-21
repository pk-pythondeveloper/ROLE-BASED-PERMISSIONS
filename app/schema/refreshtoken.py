from pydantic import BaseModel

class RefreshTokenBase(BaseModel):
    token: str

class RefreshTokenCreate(RefreshTokenBase):
    pass


class RefreshToken(RefreshTokenBase):
    id: int
    user_id: int  

    class Config:
        orm_mode = True  
