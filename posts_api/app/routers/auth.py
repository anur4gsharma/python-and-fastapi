from fastapi import HTTPException, APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from database import get_db
import schemas, models, utils

router = APIRouter(tags=['Authenication'])

@router.post("/login")
def login(credentials: schemas.UserLogin, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == credentials.email).first()

    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "User does not exist!, Create an account first")
    

    if not utils.verify(credentials.password, user.password):

        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = "Invalid Credentials")

    return "logged in"