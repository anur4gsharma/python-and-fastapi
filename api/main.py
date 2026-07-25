from datetime import datetime, timezone

from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "name": "Anurag",
        "handle": "anurag",
        "age": 18,
        "dream": "startup",
        "about": (
            "Elder brother of Anmol and the superior one. While they were mastering "
            "skills like learning jazz, I was making sure they referred to my first "
            "and last name."
        ),
        "stats": "10hrs per day work is non negotiable, still figuring out life",
        "avatar_color": "#1d9bf0",
    },
    {
        "name": "Anmol",
        "handle": "anmol",
        "age": 16,
        "dream": "IIT",
        "about": (
            "Hard worker, little distracted, wants to get a top rank and enter a top "
            "IIT CSE. He gon join Anurag's startup in the future."
        ),
        "stats": "Top ranker in his tuition and future IITian.",
        "avatar_color": "#7856ff",
    },
]

comments: list[dict] = []


def get_person(index: int) -> dict | None:
    if 0 <= index < len(posts):
        return posts[index]
    return None


@app.get("/")
def faceoff(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "comments": comments, "active": "home"},
    )


@app.get("/about/{index}")
def about_page(request: Request, index: int):
    person = get_person(index)
    if person is None:
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse(
        request,
        "about.html",
        {
            "person": person,
            "index": index,
            "posts": posts,
            "comments": comments,
            "active": "about",
        },
    )


@app.get("/overview/{index}")
def overview_page(request: Request, index: int):
    person = get_person(index)
    if person is None:
        return RedirectResponse("/", status_code=303)
    opponent_index = 1 - index
    opponent = posts[opponent_index]
    return templates.TemplateResponse(
        request,
        "overview.html",
        {
            "person": person,
            "opponent": opponent,
            "index": index,
            "posts": posts,
            "comments": comments,
            "active": "overview",
        },
    )


@app.post("/comments")
def add_comment(
    request: Request,
    author: str = Form(...),
    text: str = Form(...),
    redirect_to: str = Form("/"),
):
    author = author.strip()
    text = text.strip()
    if author and text:
        comments.insert(
            0,
            {
                "author": author,
                "text": text,
                "created_at": datetime.now(timezone.utc).strftime("%b %d, %Y · %I:%M %p"),
            },
        )
    return RedirectResponse(redirect_to or "/", status_code=303)
