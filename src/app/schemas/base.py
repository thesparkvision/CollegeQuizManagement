from pydantic import BaseModel, validator

class ErrorSchema(BaseModel):
    detail: str

def check_at_least_one_field_provided(values):
    if not any(values):
        raise ValueError(f"At least one of fields must be provided.")
    return values