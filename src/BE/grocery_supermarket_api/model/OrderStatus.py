from enum import Enum

class OrderStatus(Enum):
    CART = 1
    REMOVED = 2
    UNPAID = 3
    PAID = 4
    PACKED = 5
    PAID_DELIVERY = 6
    UNPAID_DELIVERY = 7
    DELIVERED = 8
    FEEDBACK = 9