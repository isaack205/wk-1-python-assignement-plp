def calculate_discount(price, discount_percent):
    final_price = price - (price * (discount_percent / 100))if discount_percent >= 20 else price
    print(f"Original price:", price)
    print(f"Discount:", discount_percent,"%")
    print(f"Final price:", final_price)
calculate_discount(100, 20)


print("Welcome to the discount calculator prompt!")
price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount percentage: "))
calculate_discount(price, discount_percent)
final_price = price - (price * (discount_percent / 100))

if discount_percent >= 20:
    print("Final price after discount:", final_price)
else:
    print("Final price without discount:", price)