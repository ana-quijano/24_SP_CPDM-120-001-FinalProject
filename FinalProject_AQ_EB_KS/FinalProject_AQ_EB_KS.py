from RentalShop import RentalShop
from Customer import Customer

# ---------------------------------------------------------------
# Set up the Ski and Snowboard Shop inventory
# ---------------------------------------------------------------

intTotalSkis = str(input("Enter Number of Skis in Inventory: "))
intTotalSnowboards = str(input("Enter Number of Snowboards in Inventory: "))
Inventory = RentalShop(intTotalSkis, intTotalSnowboards)
print("There are ", intTotalSkis, " skis and ", intTotalSnowboards, " in the inventory.")
print("Bob's Skis and Snowboards Shop is now open!")
