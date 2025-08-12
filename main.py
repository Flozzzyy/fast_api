
from fastapi import FastAPI

from contextlib import asynccontextmanager
from routers import router
from database import create_tables, drop_tables

@asynccontextmanager
async def lifespan(app:FastAPI):
    await drop_tables()
    print('cleaned')
    await create_tables()
    print('on')
    yield
    print('off')



app = FastAPI(lifespan=lifespan)
app.include_router(router=router)

