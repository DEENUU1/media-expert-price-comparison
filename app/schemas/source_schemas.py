from pydantic import BaseModel


class SourceOutputSchema(BaseModel):
    id: int
    url: str

    class Config:
        from_attributes = True
        orm_mode = True


class SourceInputSchema(BaseModel):
    url: str
