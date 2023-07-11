"""Customer Model Class."""


class CustomerDTO:
    def __init__(self, identifier: int, name: str, email: str, phone_number: str, address: str):
        self.identifier = identifier
        self.name = name
        self.email = email
        self.phone = phone_number
        self.address = address
