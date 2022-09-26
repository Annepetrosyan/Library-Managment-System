from abc import ABC, abstractmethod
from datetime import datetime
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
  def __init__(self, name, address, email, phone, idx):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
    self.__idx = idx


class Librarian(Person):
  def __init__(self, name, adress, email, phone, idx):
    super().__init__(name, adress, email, phone, idx)

  def add_book_item(self, book_item):
    None

  def block_member(self, member):
    None

  def un_block_member(self, member):
    None

  def set_high_demand(self, member):
    pass



class Member(Person):
  def __init__(self, name, adress, email, phone, idx):
    super().__init__(name, adress, email, phone, idx)
    self.__date_of_membership = datetime.date.today()
    self.__total_books_checkedout = 0

  def get_total_books_checkedout(self):
    return self.__total_books_checkedout

  def reserve_book_item(self, book_item):
    pass

  def increment_total_books_checkedout(self):
    pass

  def renew_book_item(self, book_item):
    pass

class Book(ABC):
  def __init__(self, ISBN, title, subject, publisher, language, number_of_pages, quantity):
    self.__ISBN = ISBN
    self.__title = title
    self.__category = BookCategory.value
    self.__publisher = publisher
    self.__language = language
    self.__number_of_pages = number_of_pages
    self.__authors = []
    self.__quantity = quantity



