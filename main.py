from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://athu2002:Ath%40rva2002@mongoproject.61degdx.mongodb.net/")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    NewDocs = []
    for doc in docs:
        NewDocs.append({
            "id": doc["_id"],
            "note": doc["note"]
        })
    return templates.TemplateResponse(
        "index.html", {"request":request, "newDocs": NewDocs}
    )