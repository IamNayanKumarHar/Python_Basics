price1 = float(input("Enter Product 1 price: "))
quantity1 = int(input("Enter Product 1 quantity: "))

price2 = float(input("Enter Product 2 price: "))
quantity2 = int(input("Enter Product 2 quantity: "))

price3 = float(input("Enter Product 3 price: "))
quantity3 = int(input("Enter Product 3 quantity: "))

discount = float(input("Enter discount percentage: "))
gst = float(input("Enter GST percentage: "))

total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * quantity3

subtotal = total1 + total2 + total3

discount_amount = subtotal * discount / 100

amount_after_discount = subtotal - discount_amount

gst_amount = amount_after_discount * gst / 100

final_amount = amount_after_discount + gst_amount


print("Product 1 Total:", total1)
print("Product 2 Total:", total2)
print("Product 3 Total:", total3)
print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Amount After Discount:", amount_after_discount)
print("GST Amount:", gst_amount)
print("Final Payable Amount:", final_amount)