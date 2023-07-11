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
        Initialize the CRUDOperations instance with the given connection string.
        """
        self.db = DatabaseConnection(connection_string).connection

    def create_record(self, db_name, table_name, data):
        """
        Create a new record in the specified database table with the given data.
        """
        cursor = self.db.cursor()

        try:
            columns = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))

            query = f"INSERT INTO {db_name}.{table_name} ({columns}) VALUES ({values})"
            values = tuple(data.values())

            cursor.execute(query, values)
            self.db.commit()
        except mysql.connector.Error as error:
            print(f"Error occurred: {error}")
            self.db.rollback()
        finally:
            cursor.close()

    def read_records(self, db_name, table_name):
        """
        Retrieve all records from the specified database table.
        """
        cursor = self.db.cursor()

        try:
            query = f"SELECT * FROM {db_name}.{table_name}"

            cursor.execute(query)
            rows = cursor.fetchall()

            records = []
            for row in rows:
                record = {
                    'column1': row[0],
                    'column2': row[1]
                }
                records.append(record)

            return records
        except mysql.connector.Error as error:
            print(f"Error occurred: {error}")
        finally:
            cursor.close()

    def update_record(self, db_name, table_name, record_id, new_data):
        """
        Update the specified record in the database table with the new data.
        """
        cursor = self.db.cursor()

        try:
            set_values = ', '.join([f"{column} = %s" for column in new_data.keys()])
            values = tuple(new_data.values())
            values += (record_id,)

            query = f"UPDATE {db_name}.{table_name} SET {set_values} WHERE id = %s"

            cursor.execute(query, values)
            self.db.commit()
        except mysql.connector.Error as error:
            print(f"Error occurred: {error}")
            self.db.rollback()
        finally:
            cursor.close()

    def delete_record(self, db_name, table_name, record_id):
        """
        Delete the specified record from the database table.
        """
        cursor = self.db.cursor()

        try:
            query = f"DELETE FROM {db_name}.{table_name} WHERE id = %s"
            values = (record_id,)

            cursor.execute(query, values)
            self.db.commit()
        except mysql.connector.Error as error:
            print(f"Error occurred: {error}")
            self.db.rollback()
        finally:
            cursor.close()
