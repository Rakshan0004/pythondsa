class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
    
    def __enter__(self):
        self.connected = True
        print(f"Connecting to {self.db_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connected = False
        print(f"Disconnecting from {self.db_name}")

with DatabaseConnection("mydb") as db:
    print("Using the database")

