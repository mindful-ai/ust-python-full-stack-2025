from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing credit card payment of INR {amount}"
    
class UPIPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing UPI payment of INR {amount}"
    
class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing PayPal payment of INR {amount}"
    


class PaymentFactory:

    @staticmethod
    def get_payment_method(method_type):
        if method_type == "CC":
            return CreditCardPayment()
        elif method_type == "UPI":
            return UPIPayment()
        elif method_type == "PP":
            return PayPalPayment()
        else:
            raise ValueError("No payment method found")



def main():
    for method in ["CC", "PP", "UPI"]:
        payment_processor = PaymentFactory.get_payment_method(method)
        print(payment_processor.process_payment(1500))

if __name__ == "__main__":

    main()