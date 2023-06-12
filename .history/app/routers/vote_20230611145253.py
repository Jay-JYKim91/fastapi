from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, database, oauth2

router = APIRouter(
    prefix="/vote",
    tages=['Vote']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
