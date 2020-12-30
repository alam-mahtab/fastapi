
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy_utils import EmailType
import datetime
from .database import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime,default=datetime.datetime.utcnow)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True)
    phone = Column(String)
    dateofbirth = Column(DateTime)
    email = Column(EmailType)
    hashed_password = Column(String)
    confirm_password = Column(String)
    is_active= Column(Boolean, default=True)
    