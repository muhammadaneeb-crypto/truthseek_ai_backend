from pydantic import BaseModel, Field, field_validator

class AskRequest(BaseModel):
    question: str = Field(min_length=2, max_length=4000)
    use_web: bool | None = None
    @field_validator("question")
    @classmethod
    def question_not_blank(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Question cannot be blank")
        return value

class Source(BaseModel):
    title: str
    url: str
    snippet: str = ""

class AskResponse(BaseModel):
    answer: str
    verification_status: str
    used_web: bool
    sources: list[Source] = []
    uncertainty_notes: list[str] = []
