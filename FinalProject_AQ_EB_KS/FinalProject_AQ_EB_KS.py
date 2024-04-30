from RentalShop import RentalShop
from Customer import Customer

# ---------------------------------------------------------------
# Set up the Ski and Snowboard Shop inventory
# ---------------------------------------------------------------

def SetUp_ShopInventory(intTotalSkis, intTotalSnowboards):
    Inventory = RentalShop(intTotalSkis, intTotalSnowboards)
    print("There are ", intTotalSkis, " skis and ", intTotalSnowboards, " in the inventory.")
    print("Bob's Skis and Snowboards Shop is now open!")

# ---------------------------------------------------------------
# Validation Functions
# ---------------------------------------------------------------

def Validate_InitialSkis(intInput):
    try:
        intInput = int(intInput)
        if intInput > 0:
            global strInitialSkisFlag
            strInitialSkisFlag = True
        else:
            print("Number of skis cannot be less than zero.")
    except ValueError:
        intInput = int(0)
        print("Number of skis must be numeric.")
    return intInput

def Validate_InitialSnowboards(intInput):
    try:
        intInput = int(intInput)
        if intInput > 0:
            global strInitialSnowboardsFlag
            strInitialSnowboardsFlag = True
        else:
            print("Number of snowboards cannot be less than zero.")
    except ValueError:
        intInput = int(0)
        print("Number of snowboards must be numeric.")
    return intInput

# ---------------------------------------------------------------
# Main Control
# ---------------------------------------------------------------

# Declare Variables

strInitialSkisFlag = bool(False)
strInitialSnowboardsFlag = bool(False)

# Get and Validate Inputs

while strInitialSkisFlag is False:
    intTotalSkis = input("Enter Number of Skis in Inventory: ")
    intTotalSkis = Validate_InitialSkis(intTotalSkis)

strInitialInventoryFlag = bool(False)

while strInitialSnowboardsFlag is False:
    intTotalSnowboards = input("Enter Number of Snowboards in Inventory: ")
    intTotalSnowboards = Validate_InitialSnowboards(intTotalSnowboards)

# Call Functions

SetUp_ShopInventory(intTotalSkis, intTotalSnowboards)
