from dto.customer_dto import CustomerDTO


class CustomerDAO:
    """Data Access Object for the Customer."""

    def __init__(self, db_manager):
        """
        Constructor for CustomerDAO class.

        """
        self.db_manager = db_manager
        self.table_name = "Customer"

    def create(self, customer: CustomerDTO):
        """
        Create a new customer in the database.
        """
        self.db_manager.create_record(table_name=self.table_name, data=vars(customer))

    def get(self, identifier) -> CustomerDTO:
        """
        Retrieve a customer from the database.
        """
        row = self.db_manager.read_record(table_name=self.table_name, identifier=identifier)
        if row:
            return CustomerDTO(**row[0])

    def update(self, customer: CustomerDTO):
        """
        Update an existing customer in the database.
        """
        self.db_manager.update_record(table_name=self.table_name, record_id=customer.identifier, new_data=vars(customer))

    def delete(self, identifier):
        """
        Delete a customer from the database.
        """
        self.db_manager.delete_record(table_name=self.table_name, record_id=identifier)
