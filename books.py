from abc import ABC
from enum import Enum

class BookCategory(Enum):
  FANTASY, MYSTERY, THRILLER, ROMANCE, WESTERNS, DYSTOPIAN, CONTEMPORARY = 1, 2, 3, 4, 5, 6, 7

class BookStatus(Enum):
  AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4

class ReservationStatus(Enum):
  WAITING, PENDING, CANCELED, NONE = 1, 2, 3, 4

class Constants:
  MAX_BOOKS_ISSUED_TO_A_USER = 5
  MAX_LENDING_DAYS = 14

class Address:
  def __init__(self, street, city, state, zip_code, country):
    self.__street_address = street
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country

class Person(ABC):
  def __init__(self, name, address, email, phone):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone


