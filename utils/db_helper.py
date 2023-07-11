import mysql.connector


class DatabaseConnection:
    """
    Singleton class for managing the database connection.
    """

    _instance = None

    def __new__(cls, connection_string):
        """
        Create a new instance of the class if it doesn't exist, or return the existing instance.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = mysql.connector.connect(**connection_string)
        return cls._instance


class DBManager:
    """
    Class for performing CRUD operations on a MySQL database.
    """

    def __init__(self, connection_string):
        """
        Initialize the DBManager instance with the given connection string.
        """
        self.db = DatabaseConnection(connection_string).connection

    def create_record(self, table_name, data):
        """
        Create a new record in the specified database table with the given data.
        """
        cursor = self.db.cursor()

        try:
            columns = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))

            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            values = tuple(data.values())

            cursor.execute(query, values)
            self.db.commit()
        except mysql.connector.Error as error:
            print(f"Error occurred: {error}")
            self.db.rollback()
        finally:
            cursor.close()

    def read_record(self, table_name, identifier):
        """
        Retrieve record from the specified database table.
        """
        cursor = self.db.cursor()

        try:
            query = f"SELECT * FROM {table_name} WHERE id=%s"

            cursor.execute(query, (identifier,))
            rows = cursor.fetchall()

            return rows
        except mysql.connector.Error as error:
            print(f"Error occurred: {error}")
        finally:
            cursor.close()

    def update_record(self, table_name, record_id, new_data):
        """
        Update the specified record in the database table with the new data.
        """
        cursor = self.db.cursor()

        try:
            set_values = ', '.join([f"{column} = %s" for column in new_data.keys()])
            values = tuple(new_data.values())
            values += (record_id,)

            query = f"UPDATE {table_name} SET {set_values} WHERE id = %s"

            cursor.execute(query, values)
            self.db.commit()
        except mysql.connector.Error as error:
            print(f"Error occurred: {error}")
            self.db.rollback()
        finally:
            cursor.close()

    def delete_record(self, table_name, record_id):
        """
        Delete the specified record from the database table.
        """
        cursor = self.db.cursor()

        try:
            query = f"DELETE FROM {table_name} WHERE id = %s"
            values = (record_id,)

            cursor.execute(query, values)
            self.db.commit()
        except mysql.connector.Error as error:
            print(f"Error occurred: {error}")
            self.db.rollback()
        finally:
            cursor.close()
