class MockUser:
    def __init__(self):
        self.first = "Juan"
        self.last = "Pérez"
        self.email = "juan@example.com"
        self.numero_telefono = "600123456"

db = MockUser()


def get_user():
    return db


def update_user(first, last, email, numero_telefono):
    db.first = first
    db.last = last
    db.email = email
    db.numero_telefono = numero_telefono
    return db
