from enum import Enum

class BookCategory(Enum):
  FANTASY, MYSTERY, THRILLER, ROMANCE, WESTERNS, DYSTOPIAN, CONTEMPORARY = 1, 2, 3, 4, 5, 6, 7

class BookStatus(Enum):
  AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4

class ReservationStatus(Enum):
  WAITING, PENDING, CANCELED, NONE = 1, 2, 3, 4


