from fastapi import Depends, FastAPI
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


class SComplaintAdd(BaseModel):
    text: str


class SComplaint(SComplaintAdd):
    id: int

complaints = []


@app.get("/")
def get_complaint():
    task = SComplaintAdd(text="Получить работу" )
    return {"data": task}


@app.post("/complaint")
async def post_complaint(
    complaint: Annotated[SComplaintAdd, Depends()]
):
    complaints.append(complaint)
    return {"ok": True}



