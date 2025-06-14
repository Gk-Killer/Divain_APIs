import psycopg2

class StockUpdate:

    @staticmethod
    def connect_to_database():
        """
        Connect to a PostgreSQL database and return the connection object.
        """
        # Connect to your postgres DB
        connection = psycopg2.connect(
            database="divain",
            user="postgres",
            password="akhil@123",
            host="localhost",
            port="5432"
        )

        cursor = connection.cursor()
        print("connection established successfully")
        return connection, cursor

    @staticmethod
    def close_connection(connection, cursor):
        """
        Close the database connection and cursor.
        """
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("Connection closed successfully")

    @staticmethod
    def fetch_stock_data():
        """
        Fetch data from the database.
        """
        try:
            connection, cursor = StockUpdate().connect_to_database()
            # Define the table name and query to fetch data
            tb_name = "stock.stock_inventory"
            get_query = f'SELECT * FROM {tb_name}'
            cursor.execute(get_query)
            records = cursor.fetchall()
            # Closing the connection
            StockUpdate().close_connection(connection, cursor)
            return records
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    @staticmethod
    def update_stock_movement(stock_id, mov_quantity, mov_type='in'):
        """
        Update stock movement in the database.
        """
        try:
            connection, cursor = StockUpdate().connect_to_database()
            # get current stock quantity
            tb_name = "stock.stock_inventory"
            get_stock_data_qry = f'SELECT quantity, item_name FROM {tb_name} WHERE sku = %s'
            cursor.execute(get_stock_data_qry, (stock_id,))
            result = cursor.fetchone()
            if result is None:
                print(f"No stock found for SKU: {stock_id}")
                StockUpdate().close_connection(connection, cursor)
                return
            current_quantity = result[0]
            mov_item_name = result[1]
            new_quantity = current_quantity + mov_quantity if mov_type == 'in' else current_quantity - mov_quantity
            # update stock quantity
            update_query = f'UPDATE {tb_name} SET quantity = %s WHERE sku = %s'
            cursor.execute(update_query, (new_quantity, stock_id))
            connection.commit()
            # insert stock movement record
            mov_tb_name = "stock.inventory_update"
            insert_query = (f'INSERT INTO {mov_tb_name} (sku, mov_quantity, mov_type, mov_item_name) VALUES (%s, %s, '
                            f'%s, %s)')
            cursor.execute(insert_query, (stock_id, mov_quantity, mov_type, mov_item_name))
            connection.commit()
            StockUpdate().close_connection(connection, cursor)
        except Exception as e:
            print(f"Error updating stock movement: {e}")

    @staticmethod
    def get_stock_movement_history():
        """
        Fetch stock movement records for a given stock ID.
        """
        try:
            connection, cursor = StockUpdate().connect_to_database()
            mov_tb_name = "stock.inventory_update"
            get_mov_query = f'SELECT * FROM {mov_tb_name}'
            cursor.execute(get_mov_query)
            records = cursor.fetchall()
            StockUpdate().close_connection(connection, cursor)
            return records
        except Exception as e:
            print(f"Error fetching stock movement: {e}")
            return None

if __name__ == "__main__":
    ins= StockUpdate()
    data = ins.fetch_stock_data()
    print(data)
    ins.update_stock_movement(stock_id='ITEM001', mov_quantity=10, mov_type='in')


