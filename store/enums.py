from enum import Enum

class OrderStatus(Enum):
    PENDING = 'pending'
    PROCESSING = 'processing'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

    @classmethod
    def choices(cls):
        return [(status.value, status.name.capitalize()) for status in cls]


class UserRole(Enum):
    CUSTOMER = 'customer'
    ADMIN = 'admin'
    PRODUCT_MANAGER = 'product_manager'
    ORDER_MANAGER = 'order_manager'

    @classmethod
    def choices(cls):
        return [(role.value, role.name.capitalize().replace("_", " ")) for role in cls]
