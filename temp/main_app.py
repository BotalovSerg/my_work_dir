import uvicorn
from fastapi import FastAPI
from databse import SessionLocal,engine, Base
from routers import user as UserRouter

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(UserRouter.router, prefix="/user")



if __name__ == '__main__':
    uvicorn.run("main_app:app", host="0.0.0.0", port=8000, reload=True, workers=3)