# Define the price and quantity
price = 299
quantity = 9

# Define the tax rate
tax_rate = 15 / 100  # 15% tax rate

# Calculate the subtotal
subtotal = price * quantity

# Calculate the tax
tax = subtotal * tax_rate

# Calculate the total
total = subtotal + tax

# Print the price, quantity, and tax rate
print(f"Price of item: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate * 100:.1f}%")  # Multiply tax_rate by 100 to show the percentage
print()
# Print the subtotal, tax, and total costs formatted as currency
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
