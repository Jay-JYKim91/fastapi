from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, database, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tages=['Vote']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    vote_query = db.query(model.Vote).filter(
        models.Vost.post_id == vote.post_id, models.Vote.user_id == current_user.id)

    if (vote.dir == 1):
        else
