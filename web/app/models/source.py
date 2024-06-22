from pydantic import BaseModel


class SourceInput(BaseModel):
    url: str


class SourceOutput(BaseModel):
    id: str
    url: str
