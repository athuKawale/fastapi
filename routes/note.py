from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse


note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    NewDocs = []
    for doc in docs:
        NewDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"]
        })
    return templates.TemplateResponse(
        "index.html", {"request":request, "newDocs": NewDocs}
    )

@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    if "important" not in formDict:
        formDict["important"] = False
    formDict["important"] = True if formDict["important"] == "on" else False
    print(formDict)
    note = conn.notes.notes.insert_one(formDict)
    success_message = "Note created successfully!"
    return RedirectResponse(url=f"/?success_message={success_message}", status_code=303)