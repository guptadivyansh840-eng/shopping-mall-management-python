print("######### WELCOME TO V-MART SHOPPING MALL #########")

category=input("Choose category [Men/Women/Children]: ")

size="N/A"

if category=="Men":
    product=input("Choose product [Shirts/Pants/Trousers]: ")
    size=input("Choose size [S/M/L/XL]: ")

elif category=="Women":
    product=input("Choose product [Shirts/Pants/Trousers]: ")
    size=input("Choose size [S/M/L/XL]: ")

elif category=="Children":
    product=input("Choose product [Clothes/Toys/Food]: ")
    if product=="Clothes":
        size=input("Choose size [S/M/L/XL]: ")
prices = {
    "Shirts": 1000,
    "Pants": 1200,
    "Trousers": 1500,
    "Clothes": 800,
    "Toys": 500,
    "Food": 300
}

payment=input("Choose payment [Card/UPI/Cash]: ")

# get price automatically
amount = prices.get(product, 0)

print("\n------ BILL ------")
print("Category:",category)
print("Product:",product)
print("Size:",size)
print("Payment:",payment)
print("Amount:",amount)
