from re import U
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, Float
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

    def __init__(self, UserId, Name, Contact, Email):
        self.UserId = UserId
        self.Name = Name
        self.ContactNum = Contact
        self.Email = Email


class City(Base):
    __tablename__ = "City"

    CityID = column(Integer, primarykey = True)
    CityName = column(String)
    StateName = column(String)

    def __init__(self, CityID, CityName, StateName):
        self.CityID = CityID
        self.CityName = CityName
        self.StateName = StateName


class Address(Base):
    __tablename__ = "Address"

    AddressID = column(String, primarykey = True)
    UserID = column(String, ForeignKey('Users.UserId'))
    CityID = column(String, ForeignKey("City.CityID"))
    Zipcode = column(Integer)
    CurrentAddress = column(String)
    Street = column(String)

    def __init__(self, AddressID,Zipcode, CurrAdd, Street):
        self.AddressID = AddressID
        self.UserID = Users.UserId
        self.CityID = City.CityID
        self.Zipcode = Zipcode
        self.CurrentAddress = CurrAdd
        self.Street = Street


class Resturant(Base):
    __tablename__ = "Resturant"

    ResturantID = column(String, primarykey = True)
    Address = column(String)
    CityID = column(String, ForeignKey("City.CityID"))
    Rating = column(Integer)
    ZipCode = column(String)

    def __init__(self, ResturantID, Address, CityID, Rating, ZipCode):
        self.ResturantID = ResturantID
        self.Address = Address
        self.CityID = CityID
        self.Rating = Rating
        self.ZipCode = ZipCode


class Menu(Base):
    __tablename__ = "Menu"

    MenuID = column(String, primarykey = True)
    ResturantID = column(String, ForeignKey("Resturant.ResturantID"))
    FoodCategoryID = column(String)
    Description = column(String)
    Price = column(Float)

    def __init__(self, Menu, RestID, FoodCatID, Desc, Price):
        self.MenuID = Menu
        self.ResturantID = RestID
        self.FoodCategoryID = FoodCatID
        self.Description = Desc
        self.Price = Price

class FoodCategory(Base):
    __tablename__ = "FoodCategory"

    FoodCategoryID = column(String, primarykey = True)
    ResturantID = column(String, ForeignKey("Resturant.ResturantID"))
    CategoryName = column(String)

    def __init__(self, FoodCat, RestID, Category):
        self.FoodCategoryID = FoodCat
        self.ResturantID = RestID
        self.CategoryName = Category

class ItemsOrdered(Base):
    __tablename__ = "ItemsOrdered"

    ItemsOrderedID = column(String, primarykey = True)
    OrderID = column(String, ForeignKey("Order.OrderID"))
    MenuID = column(String, ForeignKey("Menu.MenuID"))
    Quantity = column(Integer)
    Price = column(Float)


class Order(Base):
    __tablename__ = "Order"

    OrderID = column(String, primarykey = True)
    UserID = column(String, ForeignKey("Users.UserId"))
    ResturantID = column(String, ForeignKey("Resturant.ResturantID"))
    ItemsOrderedID = column(String, ForeignKey("ItemsOrdered.ItemsOrderedID"))
    AddressID = column(String, ForeignKey("Address.AddressID"))
    OrderStatus = column(String)
    OrderTime = column(TIMESTAMP)
    DeliveryTime = column(TIMESTAMP)
    TotalPrice = column(Float)

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

    PaymentID = column(String, primarykey = True)
    UserID = column(String, ForeignKey("Users.UserId"))
    OrderID = column(String, ForeignKey("Order.OrderID"))
    AmountToBePaid = column(Float)
    PaymentStatus = column(String)
    

    def __init__(self, PaymentID, UserID, OrderID, Amount, Status):
        self.PaymentID = PaymentID
        self.UserID = UserID
        self.OrderID = OrderID
        self.AmountToBePaid = Amount
        self.PaymentStatus = Status




Base.metadata.create_all(engine)