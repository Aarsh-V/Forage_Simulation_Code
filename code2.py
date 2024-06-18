from datetime import datetime

class Invoice:
    """Represents an invoice for a collection of services rendered to a recipient"""

    def __init__(self, sender_name, recipient_name, sender_address, recipient_address, sender_email, recipient_email):
        
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email

        self.date = datetime.now()
        self.items = []
        self.comments = []

    def add_item(self, name, price, tax):
        item = {
            "name": name,
            "price": price,
            "tax": tax
        }
        self.items.append(item)

    def calculate_total(self, discount):
        subtotal = sum(item["price"] for item in self.items)
        
        discounted_subtotal = subtotal * (1 - discount / 100)
        
        total_tax = sum(item["price"] * item["tax"] for item in self.items)
        
        total = discounted_subtotal + total_tax
        
        return total

    def add_comment(self, comment):
        """Adds a comment to the invoice"""
        self.comments.append(comment)

    def get_comments(self):
        """Returns a string representation of all comments"""
        return "\n".join(self.comments)


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
    
    invoice.add_comment("Initial consultation fee.")
    invoice.add_comment("Equipment rental for the duration of the project.")
    invoice.add_comment("Discount applied for early payment.")

    invoice_total = invoice.calculate_total(20)
    print(f"Invoice Total: {invoice_total}")
    print("Comments:")
    print(invoice.get_comments())
