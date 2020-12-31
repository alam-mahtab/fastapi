from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from . import crud, models, schemas
#from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from .database import SessionLocal, engine

from fastapi import Depends, FastAPI, HTTPException, status
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.responses import RedirectResponse


#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://fastapi-demo.herokuapp.com",
    "https://fastapi-demo.herokuapp.com/users",
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "https://localhost",
    "https://localhost:8080",
    "http://127.0.0.1:8000",
    "https://127.0.0.1:8000"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user( db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, crud.SECRET_KEY, algorithms=[crud.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = username
    except JWTError:
        raise credentials_exception
    user = crud.get_user(db, username=token_data)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if current_user.is_active == False:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user



@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(db: Session = Depends(get_db),form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me/")
async def read_users_me(current_user: models.User = Depends(get_current_active_user)):
   # user = crud.get_user(db, username=token_data)
    return current_user
    #return RedirectResponse(current_user,url="/users/me",)
    # , status_code=status.HTTP_303_SEE_OTHER)
@app.post("/users/")
def create_user(
    user: schemas.UserCreate, db: Session = Depends(get_db)
):
   return crud.create_user(db=db, user=user)
    # , status_code=status.HTTP_303_SEE_OTHER)
    #return RedirectResponse(url="/users",status_code=status)
@app.get("/users/")
async def main(current_user: models.User = Depends(get_current_active_user)):
    return {"message": "Hello " + current_user + ""}

@app.post("/login/")
def login(db: Session = Depends(get_db), form_data:OAuth2PasswordRequestForm = Depends()):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": user.username, "token_type": "bearer"}

#if user.is_authenticated:   
#@app.post("/logout/")


# def login(
#     user: schemas.Userlogin, db: Session = Depends(get_db)
# ):
#     return crud.get_user(db=db, username=username)
# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items