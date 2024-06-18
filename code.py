from datetime import datetime

class Invoice:
    """Represents an invoice for a collection of services rendered to a recipient"""

    def __init__(self, sender_name, recipient_name, sender_address, recipient_address, sender_email, recipient_email):
        # externally determined variables
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email

        # internally determined variables
        self.date = datetime.now()
        self.items = []

    def add_item(self, name, price, tax):
        # python makes working with trivial data-objects quite easy
        item = {
            "name": name,
            "price": price,
            "tax": tax
        }
        # hold on to the unmodified item for later, we'll do tax/discount calculations on an as-needed basis
        self.items.append(item)

    def calculate_total(self, discount):
        # Calculate subtotal (before tax and discount)
        subtotal = sum(item["price"] for item in self.items)
        
        # Apply discount
        discounted_subtotal = subtotal * (1 - discount / 100)
        
        # Calculate total tax
        total_tax = sum(item["price"] * item["tax"] for item in self.items)
        
        # Calculate total
        total = discounted_subtotal + total_tax
        
        return total


if __name__ == '__main__':
    invoice = Invoice(
        "Larry Jinkles",
        "Tod Hooper",
        "34 Windsor Ln.",
        "14 Manslow road",
        "lejank@billing.com",
        "discreetclorinator@hotmail.com"
    )

    invoice.add_item("34 floor building", 3400, 0.1)
    invoice.add_item("Equipment Rental", 1000, 0.1)
    invoice.add_item("Fear Tax", 340, 0.0)
    
    invoice_total = invoice.calculate_total(20)
    print(invoice_total)
