price:float = 4.99
quantity:int = 3
tax_rate:int = 15
subtotal:float = price * quantity
tax:float = subtotal * (tax_rate/100)
total:float = subtotal + tax
print("price of item: {}SR".format(round(price,2)))
print("Quantity: {}".format(quantity))
print("Tax rate: {}%".format(tax_rate))

print("Subtotal: {}SR".format(round(subtotal,2)))
print("Tax: {}SR".format(round(tax,2)))
print("Total: {}SR".format(round(total,2)))