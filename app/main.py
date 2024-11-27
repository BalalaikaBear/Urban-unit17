from fastapi import FastAPI
from routers import task, user

app = FastAPI()

#$ fastapi dev app/main.py - запуск файла

# подготовка миграции
# 1. $ alembic init app/migrations  - создание папки миграции
# 2. в файле alembic.ini прописать: sqlalchemy.url = sqlite:///taskmanager.db
# 3. в файле env.py прописать:  from app.backend.db import Base
#                               from app.models.task import Task
#                               from app.models.user import User
#                               target_metadata = Base.metadata
# 4. $ alembic revision --autogenerate -m "Initial migration"  - генерация базы данных
# 5. $ alembic upgrade head  - применение последней миграции и создание таблиц User, Task и запись текущей версии миграции

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

# позволяет подключать дополнительные внешние роуты, и легко масштабировать приложение
app.include_router(task.router)
app.include_router(user.router)