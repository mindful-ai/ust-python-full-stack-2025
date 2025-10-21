'''
Used to add extra functionality to classes in a lightweight, 
reusable way — without creating deep hierarchies
'''

class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

class Payment:
    def process(self):
        print("Processing payment...")

class SecurePayment(Payment, LoggerMixin):
    def secure_process(self):
        self.log("Starting secure payment")
        self.process()
        self.log("Payment completed")

sp = SecurePayment()
sp.secure_process()
