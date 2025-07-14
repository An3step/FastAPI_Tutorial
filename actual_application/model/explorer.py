from pydantic import BaseModel, Field

class Explorer(BaseModel):
    name: str = Field(..., min_length=1)
    country: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)