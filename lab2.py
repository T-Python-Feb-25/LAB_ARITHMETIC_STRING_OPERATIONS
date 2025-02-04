price  = 2.99
quantity = 3
tax_rate = 7.5
subtotal = (price * quantity) 
tax = subtotal * tax_rate /100
total = subtotal + tax 


phrase = "Price of item: ${}".format(round(price, 2))
print(phrase) 

phrase = "Quantity: {}".format(round(quantity, 2))
print(phrase)

phrase = "Tax rate: {}%".format(round(tax_rate, 2))
print(phrase)

print("")
phrase = "Subtotal: ${}".format(round(subtotal, 2))

print(phrase)

phrase = "Tax: ${}".format(round(tax, 2))
print(phrase)

phrase = "Total: ${}".format(round(total, 2))  # Round to 2 decimal places
print(phrase)

