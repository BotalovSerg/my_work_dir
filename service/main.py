import uvicorn
from database.connection import Base, engine
from fastapi import FastAPI
from routers.users import user_router



Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(user_router, prefix="/user")

@app.get('/')
def main():
    return {"status": 200}


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)