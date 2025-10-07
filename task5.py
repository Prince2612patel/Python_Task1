
print("------------------------------------------------------------")
name = input("Enter your name : ")
gender = input("Enter gender (M/F) : ")
age = int(input("Enter age : "))

print("------------------------------------------------------------")


product = input("Enter product name : ")
grams = float(input("Enter product grams : "))


gold_price = 12000                   
making_charge_per_gram = 845        

print("------------------------------------------------------------")
print(f"Current Gold Price (1 gram) : ₹{gold_price}")
print(f"Making Charges (1 gram)     : ₹{making_charge_per_gram}")


total_gold_rate = grams * gold_price
total_making_charge = grams * making_charge_per_gram
total_amount = total_gold_rate + total_making_charge

print("------------------------------------------------------------")
print(f"Total Gold Rate      : {grams} x {gold_price} = ₹{total_gold_rate}")
print(f"Total Making Charges : {grams} x {making_charge_per_gram} = ₹{total_making_charge}")
print(f"Total Amount         : ₹{total_gold_rate} + ₹{total_making_charge} = ₹{total_amount}")
print("------------------------------------------------------------")


discount = 0

if gender == "M" or gender == "m":       
    if age > 65:
        if 21000 < total_amount <= 31000:
            discount = 20
        elif 31000 < total_amount <= 51000:
            discount = 30
        elif total_amount > 51000:
            discount = 35
    else:
        if 21000 < total_amount <= 31000:
            discount = 10
        elif 31000 < total_amount <= 51000:
            discount = 20
        elif total_amount > 51000:
            discount = 25

elif gender == "F" or gender == "f":        
    if age > 65:
        if 21000 < total_amount <= 31000:
            discount = 25
        elif 31000 < total_amount <= 51000:
            discount = 35
        elif total_amount > 51000:
            discount = 40
    else:
        if 21000 < total_amount <= 31000:
            discount = 15
        elif 31000 < total_amount <= 51000:
            discount = 25
        elif total_amount > 51000:
            discount = 30


discount_amount = (total_gold_rate * discount) / 100
net_amount = total_amount - discount_amount


print("------------------------------------------------------------")
print("                     FINAL BILL")
print("------------------------------------------------------------")
print(f"Customer Name     : {name}")
print(f"Gender            : {gender}")
print(f"Age               : {age}")
print(f"Product Name      : {product}")
print(f"Gold Weight       : {grams} grams")
print("------------------------------------------------------------")
print(f"Total Gold Value  : ₹{total_gold_rate:.2f}")
print(f"Total Making Chrg : ₹{total_making_charge:.2f}")
print(f"Gross Amount      : ₹{total_amount:.2f}")
print("------------------------------------------------------------")
print(f"Discount (%)      : {discount}%")
print(f"Discount Amount   : ₹{discount_amount:.2f}")
print("------------------------------------------------------------")
print(f"NET AMOUNT TO PAY : ₹{net_amount:.2f}")
print("------------------------------------------------------------")



