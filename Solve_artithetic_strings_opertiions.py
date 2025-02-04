price = 10
quantity = 3
tax_rate = 15
subtotal = price * quantity
tax = subtotal * 0.15
total = subtotal + tax
print_format = f"prince of item: ${price}\nQuantity: {quantity}\ntax rate: {tax_rate}\n\nsub total: {subtotal}\ntax: {tax}\ntotal: {total}"
print(print_format)