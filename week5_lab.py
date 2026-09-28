# Week 5 Lab
# Author: Markum Reed
# Business Domain: Tech

product_name = "Laptop"
status = "pending"
quantity = 3
unit_price = 450.00
is_over_limit = unit_price * quantity > 1000.00

print(type(product_name), type(quantity), type(unit_price), type(is_over_limit))

subtotal = unit_price * quantity
tax = subtotal * 0.07
total = subtotal + tax
requires_approval = total > 1000

print(subtotal, tax, total, requires_approval)

print("=== Purchase Request Summary ===")
print(f"Product:  {product_name}")
print(f"Qty:      {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Total:    ${total:.2f}")
print(f"Requires approval: {requires_approval}")

user_quantity = float(input("Enter a new quantity: "))
new_total = unit_price * user_quantity * (1 + tax)
print(f"New total for {user_quantity}: ${new_total:.2f}")
print(f"Requires approval: {new_total > 1000}")
