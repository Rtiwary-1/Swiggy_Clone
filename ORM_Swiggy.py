from re import U
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, Float
import RandomString

engine = create_engine('mysql+pymysql://raghu:Qwerty123@localhost:3306/swiggy')

Session = sessionmaker(bind=engine)

session = Session()
Base = declarative_base()


class Users(Base):
    __tablename__ = "Users"

    UserId = Column(String(20), primary_key = True)
    Name = Column(String(20))
    ContactNum = Column(String(20))
    Email = Column(String(20))

    def __init__(self, UserId, Name, Contact, Email):
        self.UserId = UserId
        self.Name = Name
        self.ContactNum = Contact
        self.Email = Email


class City(Base):
    __tablename__ = "City"

    CityID = Column(Integer, primary_key = True)
    CityName = Column(String(20))
    StateName = Column(String(20))

    def __init__(self, CityID, CityName, StateName):
        self.CityID = CityID
        self.CityName = CityName
        self.StateName = StateName


class Address(Base):
    __tablename__ = "Address"

    AddressID = Column(String(20), primary_key = True)
    UserID = Column(String(20), ForeignKey('Users.UserId'))
    CityID = Column(Integer, ForeignKey("City.CityID"))
    Zipcode = Column(Integer)
    CurrentAddress = Column(String(20))
    Street = Column(String(20))

    def __init__(self, AddressID,Zipcode, CurrAdd, Street):
        self.AddressID = AddressID
        self.UserID = Users.UserId
        self.CityID = City.CityID
        self.Zipcode = Zipcode
        self.CurrentAddress = CurrAdd
        self.Street = Street


class Resturant(Base):
    __tablename__ = "Resturant"

    ResturantID = Column(String(20), primary_key = True)
    Address = Column(String(20))
    CityID = Column(Integer, ForeignKey("City.CityID"))
    Rating = Column(Integer)
    ZipCode = Column(String(20))

    def __init__(self, ResturantID, Address, CityID, Rating, ZipCode):
        self.ResturantID = ResturantID
        self.Address = Address
        self.CityID = CityID
        self.Rating = Rating
        self.ZipCode = ZipCode


class Menu(Base):
    __tablename__ = "Menu"

    MenuID = Column(String(20), primary_key = True)
    ResturantID = Column(String(20), ForeignKey("Resturant.ResturantID"))
    FoodCategoryID = Column(String(20))
    Description = Column(String(20))
    Price = Column(Float)

    def __init__(self, Menu, RestID, FoodCatID, Desc, Price):
        self.MenuID = Menu
        self.ResturantID = RestID
        self.FoodCategoryID = FoodCatID
        self.Description = Desc
        self.Price = Price

class FoodCategory(Base):
    __tablename__ = "FoodCategory"

    FoodCategoryID = Column(String(20), primary_key = True)
    ResturantID = Column(String(20), ForeignKey("Resturant.ResturantID"))
    CategoryName = Column(String(20))

    def __init__(self, FoodCat, RestID, Category):
        self.FoodCategoryID = FoodCat
        self.ResturantID = RestID
        self.CategoryName = Category

class ItemsOrdered(Base):
    __tablename__ = "ItemsOrdered"

    ItemsOrderedID = Column(String(20), primary_key = True)
    OrderID = Column(String(20), ForeignKey("Order.OrderID"))
    MenuID = Column(String(20), ForeignKey("Menu.MenuID"))
    Quantity = Column(Integer)
    Price = Column(Float)


class Order(Base):
    __tablename__ = "Order"

    OrderID = Column(String(20), primary_key = True)
    UserID = Column(String(20), ForeignKey("Users.UserId"))
    ResturantID = Column(String(20), ForeignKey("Resturant.ResturantID"))
    ItemsOrderedID = Column(String(20), ForeignKey("ItemsOrdered.ItemsOrderedID"))
    AddressID = Column(String(20), ForeignKey("Address.AddressID"))
    OrderStatus = Column(String(20))
    OrderTime = Column(TIMESTAMP)
    DeliveryTime = Column(TIMESTAMP)
    TotalPrice = Column(Float)

    def __init__(self, OrderID, UserID, ResturantID, ItemsID, AddressID, Status, OrderTime, Delivery, Price):
        self.OrderID = OrderID
        self.UserID = UserID
        self.ResturantID = ResturantID
        self.ItemsOrderedID = ItemsID
        self.AddressID = AddressID
        self.OrderStatus = Status
        self.OrderTime = OrderTime
        self.DeliveryTime = Delivery
        self.TotalPrice = Price



class Payment(Base):
    __tablename__ = "Payment"

    PaymentID = Column(String(20), primary_key = True)
    UserID = Column(String(20), ForeignKey("Users.UserId"))
    OrderID = Column(String(20), ForeignKey("Order.OrderID"))
    AmountToBePaid = Column(Float)
    PaymentStatus = Column(String(20))
    

    def __init__(self, PaymentID, UserID, OrderID, Amount, Status):
        self.PaymentID = PaymentID
        self.UserID = UserID
        self.OrderID = OrderID
        self.AmountToBePaid = Amount
        self.PaymentStatus = Status




Base.metadata.create_all(engine)