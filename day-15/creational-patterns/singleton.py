# Only one instance of a class is created throughout the program
# Use cases: logging, database connections. configuration object, threadpool manager


# Using a class variable
class Logger:
    _instance = None  # Class-level variable to hold the single instance

    def __new__(cls):
        # Create only one instance
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_file = "app.log"
        return cls._instance

    def write_log(self, message):
        with open(self.log_file, "a") as f:
            f.write(message + "\n")

    def __str__(self):
        return f"Logger instance with file: {self.log_file}"
    
# Using a decorator

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class DatabaseConnection:
    def __init__(self):
        print("Connecting to database...")

# --- Client code ---
logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)  # ✅ True — Both are same instance

logger1.write_log("Application started")
logger2.write_log("Another module logging")

print(logger1)
print(logger2)


db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)