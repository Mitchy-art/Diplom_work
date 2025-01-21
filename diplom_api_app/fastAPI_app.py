from fastapi import FastAPI
import uvicorn
import models
from models import users, pets
from db import engine, metadata, database
from passlib.context import CryptContext
from fastapi import Request, Form, status
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    await database.connect()
    query = models.pets.select()
    pets_ = await database.fetch_all(query)
    if not pets_:
        pets_list = [
            {"name": "Костик", "age": "2 года", "species": "cat", "breed": "Сибирская голубая гладкошерстная"},
            {"name": "Милка", "age": "3 года", "species": "dog", "breed": "Дворовая"},
            {"name": "Макси", "age": "5 лет", "species": "dog", "breed": "Дворовая"},
            {"name": "Тедди", "age": "2 месяца", "species": "cat", "breed": "Тайская"},
            {"name": "Клео", "age": "5 лет", "species": "cat", "breed": "Дворовая"},
        ]
        query = models.pets.insert()
        await database.execute_many(query, pets_list)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


app.add_middleware(SessionMiddleware, secret_key="your-secret-key")


@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("registration_page.html", {"request": request})


@app.post("/register")
async def register_post(request: Request,
                        username: str = Form(..., max_length=30),
                        password: str = Form(...),
                        password_confirm: str = Form(...),
                        age: int = Form(...),
                        email: str = Form()):
    if len(password) < 8:
        return templates.TemplateResponse("registration_page.html", {"request": request, "error": "Пароль должен быть не менее 8 символов"})
    if password != password_confirm:
        return templates.TemplateResponse("registration_page.html", {"request": request, "error": "Пароли не совпадают"})

    query = users.select().where(users.c.username == username)
    existing_user = await database.fetch_one(query)
    if existing_user:
        return templates.TemplateResponse("registration_page.html", {"request": request, "error": "Пользователь уже существует"})

    hashed_password = get_password_hash(password)
    query = users.insert().values(username=username, password_hash=hashed_password, age=age)
    await database.execute(query)
    return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("enter.html", {"request": request})


@app.post("/login")
async def login_post(request: Request, username: str = Form(...), password: str = Form(...)):
    query = users.select().where(users.c.username == username)
    user = await database.fetch_one(query)
    if not user or not verify_password(password, user["password_hash"]):
        return templates.TemplateResponse("enter.html", {"request": request, "error": "Неверный логин или пароль"})
    request.session["user"] = {"id": user["id"], "username": user["username"]}
    return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    user = request.session.get("user")
    return templates.TemplateResponse("main_page.html", {"request": request, "user": user})


@app.get("/shop", response_class=HTMLResponse)
async def shop(request: Request):
    query = pets.select()
    pet_list = await database.fetch_all(query)
    user = request.session.get("user")
    return templates.TemplateResponse("shop_page.html", {"request": request, "pets": pet_list, "user": user})

app.mount("/static", StaticFiles(directory="static"), name="static")

