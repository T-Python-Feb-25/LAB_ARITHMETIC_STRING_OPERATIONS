#Product Price 
Price = 5.85

#Product Quantity 
Quantity = 10.00

#TAX Rate 
Tax_Rate = 7.5

#Subtotal
Subtotal = Price * Quantity

#Discount Code 
Discount_Code = input("Enter your discount code /nIf you dont have code just write 'NO' ")

#If conditions 
if Discount_Code == "50":
    Discount = Subtotal * 0.50
    Subtotal -= Discount
else:
    Discount = 0 
    
Tax = Subtotal * (Tax_Rate / 100)

Total = Subtotal + Tax


#print all
print(f"\nPrice of item: ${Price:.2f}")
print(f"Quantity: {Quantity}")
print(f"TAX rate: {Tax_Rate}")

#print the discount 
if Discount > 0: 
    print(f"Discount: -${Discount:.2f}")
    
print(f"\nSubtotal: ${Subtotal:.2f}")
print(f"TAX: ${Tax:.2f}")
print(f"Total: ${Total:.2f}")