from pydantic import BaseModel

from pydantic import BaseModel, Field

class Creature(BaseModel):
    name: str = Field(..., min_length=1)
    country: str = Field(..., min_length=1)
    area: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    aka: str = Field(..., min_length=1)
