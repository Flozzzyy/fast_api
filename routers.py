from typing import Annotated
from fastapi import APIRouter, Depends
from repo import TaskRepo
from schemas import STask, STaskAdd

router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.post('')
async def add_task(task: Annotated[STaskAdd, Depends()]):
    task_id = await TaskRepo.add_one(task)
    return {'ok': 'true', 'id' : task_id}
    


@router.get('/get')
async def get_tasks() -> STask:
    tasks = await TaskRepo.get_all()
    return {'data':tasks}