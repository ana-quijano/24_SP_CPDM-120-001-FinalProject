from RentalShop import RentalShop
from Customer import Customer
import msvcrt


# ---------------------------------------------------------------
# Function to set up the Ski and Snowboard Shop inventory
# ---------------------------------------------------------------

def SetUp_ShopInventory(intTotalSkis, intTotalSnowboards, blnShopOpen):
    Inventory = RentalShop(intTotalSkis, intTotalSnowboards)
    print("Bob's Skis and Snowboards Shop is now open!\n")
    print("There are ", intTotalSkis, " skis and ", intTotalSnowboards, " in the inventory.\n")
    blnShopOpen = True
    return blnShopOpen

# ---------------------------------------------------------------
# Function to Display Navigational Selection
# display options for navigation and 
# ---------------------------------------------------------------
def NavigationalSelection(intNavigate):
    intNavigate = input("For New Customer Rental, enter 1.\nTo Return Rental, enter 2.\nTo Display Inventory, enter 3. \nTo Close Shop at End of Day, enter 4.\n")
    intNavigate = Validate_Navigation(intNavigate)
    return intNavigate 

# ---------------------------------------------------------------
# Function to Begin New Customer Rental
# ---------------------------------------------------------------

def NewCustomerRental(strFirstName, strLastName, strIDNumber, strPhoneNumber, strCouponCode, strRentalRate, intTime, intSkis, intSnowboards, dblEstimate):
    print("")
    print("Enter Customer Rental Request Details Details")
    strFirstName = input("First Name: ")
    strLastName = input("Last Name: ")
    strIDNumber = input("ID Number: ")
    strPhoneNumber = input("Phone Number: ")
    strCouponCode = input("Coupon Code: ")
    strRentalRate = input("Rental Period (Hourly, Daily, or Weekly): ")
    intTime = input("Rental Time: ")
    intSkis = input("Number of Skis: ")
    intSnowboards = input("Numbber of Snowboards: ")
    print("strRentalRate: ", strRentalRate)
    print (strFirstName, strLastName, strIDNumber, strPhoneNumber, strCouponCode, strRentalRate, intTime, intSkis, intSnowboards)
    dblEstimate = RentalShop.CalculateEstimate(strRentalRate, intSkis, intSnowboards, intTime, strCouponCode)
    print("Rental Price Estimate: ", dblEstimate)
    print("")

# ---------------------------------------------------------------
# Function to Return Rental
# ---------------------------------------------------------------

def ReturnRental():
    print("Under construction.\n")


# ---------------------------------------------------------------
# Function to Display Current Inventory
# ---------------------------------------------------------------

def DisplayInventory(intAvailableSkis, intAvailableSnowboards):
    intAvailableSkis = RentalShop.GetAvailableSkis()
    intAvailableSnowboards = RentalShop.GetAvailableSnowboards()
    print("")
    print("Current Inventory")
    print("  Available Skis: ", intAvailableSkis)
    print("  Available Snowboards: ", intAvailableSnowboards)
    print("")

# ---------------------------------------------------------------
# Function to Close Shop
# ---------------------------------------------------------------

def CloseShop(blnShopOpen):
    print("Shop is now closed.\n")
    blnShopOpen = False
    return blnShopOpen


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

def Validate_Navigation(intInput):
    try:
        intInput = int(intInput)
        if 0 < intInput < 5:
            return intInput
        else:
            print("Selection must be 1, 2, 3, or 4.")
    except ValueError:
        intInput = int(0)
        print("Selection must be 1, 2, 3, or 4.")

# ---------------------------------------------------------------
#
# Main Control
#
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Declare Variables
# ---------------------------------------------------------------

blnShopOpen = bool(False)
strInitialSkisFlag = bool(False)
strInitialSnowboardsFlag = bool(False)
strNavigateFlag = bool(False)
intNavigate = int()
intMain = int(1)

# ---------------------------------------------------------------
# Get and Validate RentalShop Class Inputs
# ---------------------------------------------------------------

while strInitialSkisFlag is False:
    intTotalSkis = input("Enter Number of Skis in Inventory: ")
    intTotalSkis = Validate_InitialSkis(intTotalSkis)

while strInitialSnowboardsFlag is False:
    intTotalSnowboards = input("Enter Number of Snowboards in Inventory: ")
    intTotalSnowboards = Validate_InitialSnowboards(intTotalSnowboards)

# ---------------------------------------------------------------
# Call Functions
# ---------------------------------------------------------------

# Call function to instantiate class RentalShop
SetUp_ShopInventory(intTotalSkis, intTotalSnowboards, blnShopOpen)

# Get intNavigate to determine next action
#(1 for new customer rental, 2 for return rental, 3 for inventory display, 4 for close shop)
# intNavigate = NavigationalSelection(intNavigate)

# Depending on action selected, call appropriate function
intNavigate = NavigationalSelection(intNavigate)

if intNavigate == 1:
    # add new customer to a list of customers
    NewCustomerRental(strFirstName = "", strLastName = "", strIDNumber = "", strPhoneNumber = "", strCouponCode = "", strRentalRate = "", intTime = 0, intSkis = 0, intSnowboards = 0, dblEstimate = 0)
else:
    # This does not work yet
    if intNavigate == 2:
        ReturnRental()
    else:
        # This works!
        if intNavigate == 3:
            DisplayInventory(intAvailableSkis = 0, intAvailableSnowboards = 0)
        else:
            # This does not work yet
            if intNavigate == 4:
                CloseShop()
                
