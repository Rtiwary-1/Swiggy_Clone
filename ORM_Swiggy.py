from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.sql.expression import column
import RandomString

engine = create_engine('mysql://raghu:Qwerty123@localhost:3306/sqlalchemy')

Session = sessionmaker(bind=engine)

session = Session()
Base = declarative_base()


class Users(Base):
    __tablename__ = "Users"

    UserId = column(String, primary_key = True)
    Name = column(String)
    ContactNum = column(String)
    Email = Column(String)

    def __init__(self, Name, Contact, Email):
        self.UserId = RandomString()
        self.Name = Name
        self.ContactNum = Contact
        self.Email = Email


class Address(Base):
    __tablename__ = "Address"

    UserID = column(String)
    CityID = column(String)
    Zipcode = column(Integer)
    CurrentAddress = column(String)
    Street = column(String)

    def __init__(self, Zipcode, CurrAdd, Street):
        self.UserID = Users.UserId
        self.CityID = City.CityID
        self.Zipcode = Zipcode
        self.CurrentAddress = CurrAdd
        self.Street = Street


class City(Base):
    __tablename__ = "City"

    CityID = column(String)
    CityName = column(String)
    StateName = column(String)